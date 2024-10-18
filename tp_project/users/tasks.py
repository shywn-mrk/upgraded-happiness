from celery import shared_task
# from django.core.mail import send_mail
from django.core.cache import cache
import random

from .models import User


@shared_task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()

@shared_task()
def send_otp_email(username):
    # Generate a random OTP
    otp = random.randint(100000, 999999)

    # Store OTP in Django cache (Redis) with an expiration time (e.g., 5 minutes)
    cache_key = f'otp_{username}'
    cache.set(cache_key, otp, timeout=300)  # 300 seconds = 5 minutes
    
    # Send OTP via email (or SMS if needed)
    # from django.core.mail import send_mail
    # send_mail(
    #     subject='Your OTP Code',
    #     message=f'Your OTP code is {otp}',
    #     from_email='no-reply@yourdomain.com',
    #     recipient_list=[user_email],
    # )
    
    # Returning the OTP for logging or debugging (you can remove this in production)
    return otp
