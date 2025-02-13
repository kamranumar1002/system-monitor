from django.contrib import admin
from .models import TblClients, TblSites, TblSystem, TblBenchmark, TblEvent
# Register your models here.

@admin.register(TblBenchmark)
class TblBenchmarkAdmin(admin.ModelAdmin):
    list_display = ('bnc_id', 'bnc_process', 'bnc_normal', 'bnc_warning', 'bnc_critical')
    search_fields = ('bnc_process', 'bnc_normal', 'bnc_warning', 'bnc_critical')
    list_filter = ('bnc_process', 'bnc_normal', 'bnc_warning', 'bnc_critical')

@admin.register(TblEvent)
class TblEventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'system_id', 'event_value', 'event_type', 'bnc_id',  'event_creation_date')
    search_fields = ('system_id', 'bnc_id', 'event_type', 'event_email')
    list_filter = ('event_type', 'event_emaildelivery', 'event_creation_date')

@admin.register(TblClients)
class TblClientsAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'client_name', 'client_email')
    search_fields = ('client_name', 'client_email')

@admin.register(TblSites)
class TblSitesAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'site_name', 'site_address')
    search_fields = ('site_name', 'site_address')

@admin.register(TblSystem)
class TblSystemAdmin(admin.ModelAdmin):
    list_display = ('system_id', 'system_name', 'site_id')
    search_fields = ('system_name', 'site_id')
    list_filter = ('site_id',)