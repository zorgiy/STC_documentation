from django.contrib import admin

from apps.catalog.models import Partners, Companies, Workers

admin.site.register(Partners)
admin.site.register(Companies)
admin.site.register(Workers)

