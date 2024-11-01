from django.db import models
import string
import random

class ShortURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choices(characters, k=6))
            if not ShortURL.objects.filter(short_url=short_url).exists():
                break
        return short_url

    def __str__(self):
        return f'{self.short_url} -> {self.original_url}'
