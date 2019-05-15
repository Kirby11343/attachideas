from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(primary_key=True, max_length=250, unique=True)

    def slug(self):
        return slugify(self.user.username)

    def __str__ (self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        img = img.convert("RGB")

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path, "JPEG")

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

