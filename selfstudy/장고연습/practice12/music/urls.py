from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.artist_cr),
    path('artists/<int:artist_pk>/', views.artist_r),
    path('artists/<int:artist_pk>/music/', views.music_c),
    path('music/', views.music_r),
    path('music/<int:music_pk>/', views.music_urd),

]
