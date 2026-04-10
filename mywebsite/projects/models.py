from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/') # Gambar masuk ke folder media/projects/
    github_link = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=200, help_text="Contoh: Django, IoT, Python")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): # Gunakan __str__ bukan __clstr__
        return self.title