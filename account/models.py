from django.db import models
from django.contrib.auth.models import User
import json
import urllib

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    gravatar_url = models.CharField(max_length=100)
    
    facebook = models.CharField(max_length=100, default="Facebook")
    google = models.CharField(max_length=100, default="Google")
    yahoo = models.CharField(max_length=100, default="Yahoo")

    exp = models.IntegerField(null=True, default=0)
    lvl = models.IntegerField(default=1)
    
    achieve_points = models.IntegerField(default=0)

    facebook_id = models.BigIntegerField(null=True)
    access_token = models.CharField(max_length=150)

    def get_facebook_profile(self):
        fb_profile = urllib.urlopen('https://graph.facebook.com/me?access_token=%s' % self.access_token)
        return json.load(fb_profile)
