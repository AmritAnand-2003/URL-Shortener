from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import URL
from .serializers import URLShortenerSerializer, CustomURLShortenerSerializer, URLStatsSerializer
from .helpers.helper import generate_short_url
from .constants import BASEURL
from .helpers.helper import validate_url


class ShortenURLView(APIView):
    """
    API to shorten a URL. Returns the existing short URL if already present, otherwise generates a new one.
    """
    serializer_class = URLShortenerSerializer
    def post(self, request):
        serializer = URLShortenerSerializer(data=request.data)
        if serializer.is_valid():
            original_url = serializer.validated_data['original_url']
            url_entry = URL.objects.filter(original_url=original_url).first()
            if url_entry and not url_entry.is_expired():
                return Response(
                    {"short_url": BASEURL +  url_entry.short_url, "message": "URL already exists."},
                    status=status.HTTP_200_OK
                )
            short_url = generate_short_url(original_url)
            while URL.objects.filter(short_url=short_url).exists():
                short_url = generate_short_url(original_url)

            serializer.validated_data['short_url'] = short_url
            shortened_url = serializer.save()

            return Response(
                {
                    "original_url": shortened_url.original_url,
                    "short_url": BASEURL + shortened_url.short_url,
                    "expires_at": shortened_url.expires_at,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedirectURLView(APIView):
    def get(self, request, short_url):
        shortened_url = get_object_or_404(URL, short_url=short_url)
        if shortened_url.is_expired():
            return Response({"error": "This URL has expired."}, status=status.HTTP_410_GONE)
        shortened_url.access_count += 1
        shortened_url.save()
        return redirect(shortened_url.original_url)
    

class URLstats(APIView):
    def get(self, request, short_url):
        shortened_url = get_object_or_404(URL, short_url=short_url)
        return Response(
            {
                "access_count": shortened_url.access_count,
            }
        )
    
class CustomShortenedURLAPIView(APIView):
    """
    API endpoint for creating custom shortened URLs.
    Accepts requests only if custom URL is unique.
    Format: 216.48.179.47:8000/short_url where short_url is your custom URL path
    """
    serializer_class = CustomURLShortenerSerializer
    def post(self, request):
        data = request.data
        custom_short_url = data.get('short_url')
        original_url = data.get('original_url')
        if not original_url or  not validate_url(original_url):
            return Response(
                {"error": "Provided URL is not a valid URL."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not custom_short_url or not validate_url(custom_short_url):
            return Response(
                {"error": "Provided short URL is not a valid URL."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # For checking if the custome short URL is already being used
        if URL.objects.filter(short_url=custom_short_url).exists():
            return Response(
                {"error": "Custom short URL already exists. Try some other short URL."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CustomURLShortenerSerializer(data={
            "original_url": original_url,
            "short_url": custom_short_url,
            "ttl": data.get("ttl")
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class URLStatsView(APIView):
    """
    View to fetch statistics for a given short URL via POST request.
    """
    serializer_class = URLStatsSerializer
    def post(self, request):
        short_url = request.data.get('short_url')
        
        if not short_url:
            return Response(
                {"error": "The 'short_url' field is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if short_url.startswith(BASEURL):
            short_url = short_url[len(BASEURL):]
        url_stats = get_object_or_404(URL, short_url=short_url)
        serializer = URLStatsSerializer(url_stats)
        return Response(serializer.data, status=status.HTTP_200_OK)


class HomePageView(TemplateView):
    template_name = 'home.html'

