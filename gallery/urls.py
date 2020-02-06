from django.conf.urls import include, url

from gallery.views import ImageView, ImageList, AlbumView, AlbumList, ImageCreate

app_name = 'gallery'
urlpatterns = [
    url(r'^$', AlbumList.as_view(), name='album_list'),
    url(r'^images/', ImageList.as_view(), name='image_list'),
    url(r'^image/<int:pk>/<slug>', ImageView.as_view(), name='image_detail'),
    url(r'^upload/', ImageCreate.as_view(), name='image_upload'),
    url(r'^album/<int:pk>/<slug>/', AlbumView.as_view(), name='album_detail'),
    url(r'^album/<int:apk>/<int:pk>/<slug>', ImageView.as_view(), name='album_image_detail')
]
