from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import URL
from .serializers import URLShortenerSerializer
from .helpers.helper import generate_short_url

class ShortenURLView(APIView):
    serializer_class = URLShortenerSerializer
    def post(self, request):
        breakpoint()
        serializer = URLShortenerSerializer(data=request.data)
        if serializer.is_valid():
            original_url = serializer.validated_data['original_url']
            url_entry = URL.objects.filter(original_url=original_url).first()
            if url_entry and not url_entry.is_expired():
                return Response(
                    {"short_url": url_entry.short_url},
                    status=status.HTTP_200_OK
                )
            short_url = generate_short_url(original_url)
            while URL.objects.filter(short_url=short_url).exists():
                short_url = generate_short_url()

            # Save the new entry with the generated short URL and optional TTL
            serializer.validated_data['short_url'] = short_url
            shortened_url = serializer.save()

            return Response(
                {
                    "original_url": shortened_url.original_url,
                    "short_url": shortened_url.short_url,
                    "expires_at": shortened_url.expires_at,
                },
                status=status.HTTP_201_CREATED,
            )
            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RedirectURLView(APIView):
    def get(self, request, short_url):
        # breakpoint()
        shortened_url = get_object_or_404(URL, short_url=short_url)

        if shortened_url.is_expired():
            return Response({"error": "This URL has expired."}, status=status.HTTP_410_GONE)

        # Increment access count and redirect
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