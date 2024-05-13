from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.conf import  settings

def hello_view(request):
    return HttpResponse("Hello")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

# Amazon OAuth2 credentials
AMAZON_CLIENT_ID = settings.AMAZON_CLIENT_ID
AMAZON_CLIENT_SECRET = settings.AMAZON_CLIENT_SECRET
REDIRECT_URI = 'https://www.youtube.com/'

class AmazonLoginView(APIView):
    def get(self, request):
        scopes = 'profile'

        # Redirect user to Amazon login page with specified scopes
        auth_url = f'https://www.amazon.com/ap/oa?client_id={AMAZON_CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={scopes}'
        return JsonResponse({'auth_url': auth_url})
        #return redirect(auth_url)


# class AmazonCallbackView(APIView):
#     def get(self, request):
#         # Retrieve authorization code from query parameters
#         code = request.GET.get('code')
#
#         # Exchange authorization code for access token
#         token_url = 'https://api.amazon.com/auth/o2/token'
#         data = {
#             'grant_type': 'authorization_code',
#             'code': code,
#             'client_id': AMAZON_CLIENT_ID,
#             'client_secret': AMAZON_CLIENT_SECRET,
#             'redirect_uri': REDIRECT_URI
#         }
#         response = requests.post(token_url, data=data)
#         token_data = response.json()
#
#         # Use access token to access user information
#         access_token = token_data['access_token']
#         profile_url = 'https://api.amazon.com/user/profile'
#         headers = {'Authorization': f'Bearer {access_token}'}
#         profile_response = requests.get(profile_url, headers=headers)
#         profile_data = profile_response.json()
#
#         # Handle user information as needed
#         user_email = profile_data['email']
#         # etc.
#
#         return Response({'message': 'User authenticated successfully'}, status=status.HTTP_200_OK)
