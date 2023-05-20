from django.urls import path
from . import views 
from django.contrib.sitemaps.views import sitemap 

from users.sitemap import BlogSitemap

# a dictionary of sitemaps
sitemaps = {
    'blog': BlogSitemap,
}
urlpatterns = [
    path('', views.index_view, name='index' ),
    path('signup', views.signup_view, name='signup' ),
    path('login', views.login_view, name='login' ),
    path('logout', views.logout_view, name='logout' ),
    path('qrcode', views.qrcode_view, name='qrcode'),
    path('pricing', views.pricing_view, name='pricing'),
    path('waitlist-success', views.waitlist_view, name='waitlist'),
    path('api-documentations', views.documentation_view, name='docs'),
    path("sitemap.xml", sitemap,{"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),
    path('api/v1/images/', views.api_view.as_view(), name='api' ),
]
