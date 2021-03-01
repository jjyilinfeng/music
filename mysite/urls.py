from django.urls import path
from mysite import views

handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
urlpatterns = {
    path('index/', views.index),
    path('index/lyric_download', views.lyric_download),
    path('test/', views.test),
    path('website_manual/', views.website_manual),
    path('songs/', views.songs),
    path('message/', views.message),
    path('message/create_message/', views.create_message),
    path('music_key_statistics/', views.music_key_statistics)
}


