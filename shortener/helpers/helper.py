import re
import validators
import random, string

def validate_url(url):
    # Check if the URL starts with a valid scheme
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL must start with http:// or https://")

    # Validate using the validators library (more comprehensive)
    if not validators.url(url):
        raise ValueError("Provided URL is not a valid URL.")

    # Optionally, add a regex check for custom requirements
    url_pattern = re.compile(
        r'^(http|https)://'  # Scheme
        r'([\w-]+\.)+[\w-]{2,4}'  # Domain
        r'(/[\w\-./?%&=]*)?$'  # Path
    )
    if not url_pattern.match(url):
        raise ValueError("URL does not match the required pattern.")

    return url

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