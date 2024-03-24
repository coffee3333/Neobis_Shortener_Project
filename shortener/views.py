from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShortenedURLSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import redirect
from .models import ShortenedURL
from rest_framework import generics



class SchortnerList(generics.ListAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer

class ShortenURL(APIView):
    @swagger_auto_schema(request_body=ShortenedURLSerializer, 
                         responses={200: openapi.Response('Response Description', ShortenedURLSerializer)})
    def post(self, request, *args, **kwargs):
        serializer = ShortenedURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            current_site = request.build_absolute_uri('/')[:-1]
            short_id = serializer.data['short_id']
            response_data = {
                'short_url': f"{current_site}/api/{short_id}"
            }
            return Response(response_data)
        return Response(serializer.errors)

class RedirectView(APIView):
    def get(self, request, short_id, *args, **kwargs):
        try:
            short_url = ShortenedURL.objects.get(short_id=short_id)
            return redirect(short_url.original_url)
        except ShortenedURL.DoesNotExist:
            return Response({'error': 'Shortened URL does not exist.'}, status=404)