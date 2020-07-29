from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Design(models.Model):
	title=models.CharField(max_length=60)
	description=models.TextField(blank=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	image_preview=models.ImageField(upload_to='design_previews')
	datetime_posted=models.DateTimeField(auto_now_add=True, blank=True)
	file=models.FileField(upload_to='design_files')

	def save(self, **kwargs):
		super().save()
		img = Image.open(self.image_preview.path)
		if img.width > 300 or img.height > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image_preview.path)

