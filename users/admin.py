from django.contrib import admin
from .models import Mentee
from .models import Mentor
from .models import Lesson

# Register your models here.
admin.site.register(Mentee)
admin.site.register(Mentor)
admin.site.register(Lesson)
