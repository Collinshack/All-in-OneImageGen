from django.contrib.sitemaps import Sitemap
from users.models import BlogPost

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return BlogPost.objects.filter()

    def lastmod(self, obj):
        return obj.publish_date


