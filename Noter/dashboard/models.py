from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
from html2text import html2text
from django.utils.html import strip_tags

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    content = models.TextField()
    shorter_content = models.TextField(blank=True)  # Dodane pole
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Note.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.title) + str(uuid.uuid4())[:8]

        self.shorter_content = strip_tags(self.content)[:200] + '...'

        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return self.title