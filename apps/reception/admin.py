from django.contrib import admin

from apps.reception.models import Incoming, Outgoing, Order

admin.site.register(Incoming)
admin.site.register(Outgoing)
admin.site.register(Order)
