from django.urls import path
from common.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('like/<int:photo_id>/', like_photo, name='like photo'),
    path('share/<int:photo_id>/', share_photo, name='share photo'),
    path('comment/<int:photo_id>/', comment_photo, name='comment photo'),
]
