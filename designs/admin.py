from django.contrib import admin
from users.models import Profile
from designs.models import Design
# Register your models here.
admin.site.register(Profile)
admin.site.register(Design)