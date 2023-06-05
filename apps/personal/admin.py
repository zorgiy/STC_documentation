from django.contrib import admin

from apps.personal.models import LogActs, LogContract, LogAddAgreements, LogOrdersK, LogOrdersLS, LogOrdersSh, \
    LogWorkContracts, RegisterFinSupport

admin.site.register(LogActs)
admin.site.register(LogContract)
admin.site.register(LogAddAgreements)
admin.site.register(LogOrdersK)
admin.site.register(LogOrdersLS)
admin.site.register(LogOrdersSh)
admin.site.register(LogWorkContracts)
admin.site.register(RegisterFinSupport)
