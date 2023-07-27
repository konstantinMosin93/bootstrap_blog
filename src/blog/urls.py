from django.urls import path

from .views import MainView
from .views import PostDetailView
from .views import SignUpView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
