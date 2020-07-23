from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	image=models.ImageField(default='default_profile.jpg', upload_to='profile_pics', verbose_name='Select your profile image')

	def save(self, **kwargs):
		super().save()
		img=Image.open(self.image.path)
		if img.width > 300 or img.height > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)