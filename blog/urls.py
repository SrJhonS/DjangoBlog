from django.conf.urls import include, url
from . import views

urlpatterns = [
	#url(r'^$', views.post_list, name='post_list'),
	url(r'^$', views.PostList.as_view(), name='post_list'),
	#url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'), #Ver post
	url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'), #Ver post
	#url(r'^post/new/$', views.post_new, name='post_new'), #Nuevo post
	url(r'^post/new/$', views.PostCreate.as_view(), name='post_new'), #Nuevo post
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'), #Editar post
	#url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'), #Eliminar post
	#url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post_delete'), #Eliminar post

]