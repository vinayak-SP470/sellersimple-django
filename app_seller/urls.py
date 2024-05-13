from django.urls import path
from .views import hello_view, AmazonLoginView

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('amazon/login/', AmazonLoginView.as_view(), name='amazon-login'),
    #path('amazon/callback/', AmazonCallbackView.as_view(), name='amazon-callback'),
]