import re
import validators
import random, string
from shortener.models import URL
from django.db import transaction

def validate_url(url):
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL must start with http:// or https://")
    if not validators.url(url):
        raise ValueError("Provided URL is not a valid URL.")
    url_pattern = re.compile(
        r'^(http|https)://' 
        r'([\w-]+\.)+[\w-]{2,4}' 
        r'(/[\w\-./?%&=]*)?$' 
    )
    if not url_pattern.match(url):
        raise ValueError("URL does not match the required pattern.")
    return url


def create_shortened_url(serializer):
    try:
        with transaction.atomic():
            short_url = generate_short_url_base62()
            serializer.validated_data['short_url'] = short_url
            shortened_url = serializer.save()
            return shortened_url
    except Exception as e:
        print(f"Error creating shortened URL: {e}")
        return None

def generate_short_url_base62():
    last_url = URL.objects.order_by('-id').first()
    next_id = (last_url.id if last_url else 0) + 100000000001

    short_url = base_62_encode(next_id)
    while URL.objects.filter(short_url=short_url).exists():
        next_id += 1
        short_url = base_62_encode(next_id)
    return short_url

def base_62_encode(number):
    chars = string.digits + string.ascii_letters
    result = ""
    while number > 0:
        number, remainder = divmod(number, 62)
        result = chars[remainder] + result
    return result

def generate_short_url(url, length=7):
    # Generate a short URL using a custom algorithm
    prefix = "http://127.0.0.1:8000/"
    # Remove the scheme from the URL
    url = re.sub(r'^https?://', '', url)

    # Generate a random string of the specified length
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    # Combine the short code with the URL
    url = short_code
    return url