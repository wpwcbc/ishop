from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'ishop'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^additem$', views.additem, name="additem"),
    path('myitem', views.myitem, name="myitem"),
    path('itemsdetail/<int:IID>', views.itemsdetail, name="itemsdetail"),
    path('myitemsdetail/<int:IID>', views.myitemsdetail, name="myitemsdetail"),
    path('myitemsdetail/edititem/<int:IID>', views.edititem, name="edititem"),
]

urlpatterns += staticfiles_urlpatterns()