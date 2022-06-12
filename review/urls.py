
from django.conf import settings
from django.conf.urls import url
from  django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$',views.index, name='index'),
    url(r'^home/',views.home, name='home'),
    url(r'^main/',views.landing_page,name = 'landing_page'),
    url(r'^project/',views.project,name = 'project'),
    url(r'^edit_profile/',views.editprofile,name = 'edit_profile'),
    url(r'^profile/',views.profile,name = 'profile'),
    url(r'^search/',views.search,name = 'search'),
    url(r'^display/',views.display_search,name = 'display_search'),
    url(r'^details/(\d+)',views.details,name = 'details'),
    # url(r'^details/(\d+)',views.rating,name = 'rate-project'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)