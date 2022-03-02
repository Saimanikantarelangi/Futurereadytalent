from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from myapi.models import Posts

class PostSitemap(Sitemap):
    def items(self):
        return Posts.objects.all()
    def latestmod(self,obj):
        return obj.date