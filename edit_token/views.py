from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['simsu'] = user.id
        token['1'] = user.username
        token['2'] = user.password
        # ...

        return token
    

@api_view(['GET', 'POST'])
def get_user_info(request):
   if request.method == 'POST':
        serializer = MyTokenObtainPairSerializer()
        return Response(serializer.validate(request.data))
   return Response({"message": "Hello, world!"})


def get_user_page(request):
    return render(request, 'user.html')

