from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Design(models.Model):
	title=models.CharField(max_length=60)
	description=models.TextField(blank=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	image_preview=models.ImageField(default='default.jpg', upload_to='design_previews')
	datetime_posted=models.DateTimeField(auto_now_add=True, blank=True)
	file=models.FileField(upload_to='design_files')