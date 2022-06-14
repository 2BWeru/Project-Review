from django.urls import reverse
from unittest import loader
from django.http import  HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import Rateform
from review.models import Profile, Projects, Review
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectsSerializer


#API REQUEST
class MerchList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data) 

#API REQUEST
class ProjectsList(APIView):
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects, many=True)
        return Response(serializers.data) 




# Create your views here.
def index(request):

    return render(request, 'index.html')

# home
# @login_required(login_url='/accounts/login/')
# def home(request):

#     return render(request, 'home.html')

# landing page
@login_required(login_url='/accounts/login/')
def landing_page(request):

    projects=Projects.objects.all()
    profiles=Profile.objects.all()

    return render(request, 'home/landing_page.html',{"projects":projects,"profiles":profiles})

# profile
@login_required(login_url='/accounts/login/')
def profile(request):
    user=request.user
    profiles=Profile.objects.all()
    project=Projects.objects.all()
    return render(request, 'profile/profile.html',{'profiles':profiles,"project":project,"user":user})

# edit_profile
@login_required(login_url='/accounts/login/')
def editprofile(request):
    if request.method == "POST":
        prod = Profile()
        prod.fullname = request.POST.get('fullname'),
        prod.bio = request.POST.get('bio')
        prod.contacts = request.POST.get('contacts') 

        if len(request.FILES) != 0:
            prod.avatar = request.FILES.get('avatar')

        prod.save()
        
        return redirect('profile')

    return render(request,'profile/edit_profile.html')

# add post
@login_required(login_url='/accounts/login/')
def project(request):
    if request.method == 'POST':
        prod = Projects()
        prod.title = request.POST.get('title')
        prod.link = request.POST.get('link')
        prod.description = request.POST.get('description')

        if (request.FILES) != 0 :
            prod.landing_page = request.FILES.get('landing_page')
        
        prod.save()
        
        return redirect('landing_page')
    return render(request, 'home/addproject.html') 


# search
def search(request):
        if "projects" in request.GET and request.GET["projects"]:
            searched_item=request.GET["projects"]
            projects= Projects.search_by_title(searched_item)
            message = f"{searched_item}"


            return render(request, 'search.html',{"message":message,"projects":projects})
        else:
            message = "Kindly input a search term to get any results"
            return render(request,'search.html',{"message":message})



#display_search
def display_search(request):

    projects=Projects.objects.all()

    return render(request,'search.html',{"projects":projects})

# rating
@login_required(login_url='/accounts/login/')
def details(request,id):
    projects=Projects.objects.filter(id=id)
    # rating=Review.total_rating(self=id)
    # Re.objects.all().aggregate(Avg('price'))
    user=request.user

    if request.method == "POST":
        form = Rateform(request.POST)
        if form.is_valid():
            rate_by_design=form.save(commit=False)
            rate_by_usability=form.save(commit=False)
            rate_by_content=form.save(commit=False)
            reviews=form.save(commit=False)
            
            rate_by_design.user=user
            rate_by_usability.user=user
            rate_by_content.user=user
            reviews.user=user


            # rate_by_design.projects=projects
            # rate_by_usability.projects=projects
            # rate_by_content.projects=projects


            rate_by_design.save()
            rate_by_usability.save()
            rate_by_content.save()
            reviews.save()


            
        return HttpResponseRedirect(reverse('details', args=(id,)))
    else:
        form=Rateform()

    # template=loader.get_template('home/details.html')
    
    context={
        'form':form,
        'review':review,
        'projects':projects,
        # 'rating':rating,
        # "template":template,

    }

    return render(request,'home/details.html',context)


# logout
@login_required(login_url='/accounts/login/')
def logout(request):
    return render(request, 'registration/registration_form.html')


