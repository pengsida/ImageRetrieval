from django.conf.urls import url
from . import search
 
from . import view
 
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^search$', search.search),
]