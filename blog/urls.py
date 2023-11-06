
from django.urls import re_path

from blog import views
urlpatterns = [

    re_path(r'^$',views.home,name = 'home'),
    re_path(r'^about/$',views.about,name='about'),
    re_path(r'^article/(?P<article_id>[0-9]+)/$',views.show_article,name = 'article'),
]