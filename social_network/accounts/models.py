from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):	
    """Customer's profile"""	

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Not_specified', 'Not_specified'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone_number = models.CharField(max_length=13)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=13,choices=GENDER_CHOICES, default='Not_specified')

    def __str__(self):
        return f'{self.id} {self.user}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()