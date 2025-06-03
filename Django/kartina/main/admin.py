from django.contrib import admin

from .models import modern_picture, classic_picture, abstract_picture, portret_picture, favorites_picture

admin.site.register(modern_picture)
admin.site.register(classic_picture)
admin.site.register(abstract_picture)
admin.site.register(portret_picture)
admin.site.register(favorites_picture)