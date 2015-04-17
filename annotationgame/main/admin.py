from django.contrib import admin
import models

# Register your models here.
for model in [models.Answer,models.Annotation,models.Streak]:
    admin.site.register(model)