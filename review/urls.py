from django.conf import settings
from django.conf.urls import  url
from  django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    url('^$',views.index, name='index'),
    url(r'^main/',views.landing_page,name = 'landing_page'),
    url(r'^project/',views.project,name = 'project'),
    url(r'^edit_profile/',views.editprofile,name = 'edit_profile'),
    url(r'^profile/',views.profile,name = 'profile'),
    url(r'^logout/$', LogoutView.as_view(),  name='logout'),
    url(r'^search/',views.search,name = 'search'),
    url(r'^display/',views.display_search,name = 'display_search'),
    url(r'^details/(\d+)',views.details,name = 'details'),
    url(r'^api/profiles/$', views.MerchList.as_view()),
    url(r'^api/projects/$', views.ProjectsList.as_view())

    # url(r'^details/(\d+)',views.rating,name = 'rate-project'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)