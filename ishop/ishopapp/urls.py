from ishopapp.views import index, itemsdetail
from django.conf.urls import url
from django.urls import path
urlpatterns = [
    url(r'^$', index),
    path('itemsdetail/<int:IID>', itemsdetail)
]