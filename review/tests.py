from django.test import TestCase
from matplotlib.pyplot import title

from review.views import landing_page
from .models import Projects,Profile,Review


# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.BettyWeru= Profile(fullname="Betty Weru",bio="I love tech",avatar="static/images/")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.BettyWeru,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.BettyWeru.save_profile()
        images = Profile.objects.all()
        self.assertTrue(len(images) > 0)

    # delete model
    def test_delete_profile(self):
        Profile.objects.all().delete()


class ProjectsTestClass(TestCase):

    # set up method
    def setUp(self):
        self.Pitch=Projects(description='pitch website',landing_page='static/images/',title='pitch',link='www.pitch.com',created='12 June 2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.Pitch,Projects))

    # save
    def test_save_projects(self):
        self.Pitch.save_project()
        landing_page=Projects.objects.all()
        self.assertTrue(len(landing_page) > 0)

    def test_delete_project(self):
        Projects.objects.all().delete()
