# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TblBenchmark(models.Model):
    bnc_id = models.AutoField(primary_key=True)
    bnc_process = models.CharField(
        unique=True, max_length=255, )
    bnc_normal = models.IntegerField(blank=True, null=True, default=40)
    bnc_warning = models.IntegerField(blank=True, null=True, default=60)
    bnc_critical = models.IntegerField(blank=True, null=True, default=80)

    class Meta:
        db_table = 'tbl_benchmark'
        verbose_name = 'Benchmark'
        verbose_name_plural = 'Benchmarks'
    
    def __str__(request):
        return(str(request.bnc_id))


class TblClients(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(
        max_length=255, )
    client_email = models.CharField(
        max_length=200, )
    client_contact = models.CharField(
        max_length=30, )
    client_address = models.TextField()
    client_creation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        unique_together = (('client_name', 'client_email'),)

    def __str__(request):
        return(request.client_name)


class TblEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    site_id = models.IntegerField()
    system_id = models.IntegerField()
    bnc_id = models.IntegerField()
    event_value = models.IntegerField()
    event_type = models.CharField(
        max_length=15, )
    event_email = models.TextField()
    event_emaildelivery = models.IntegerField(default=0)
    event_creation_date = models.DateTimeField(blank=True, null=True)
    tmp_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


class TblEventTmp(models.Model):
    client = models.CharField(
        max_length=255, )
    site = models.CharField(max_length=255, )
    system = models.CharField(
        max_length=255, )
    bench = models.CharField(max_length=255, )
    event_value = models.IntegerField()
    event_email = models.TextField()
    event_emaildelivery = models.CharField(
        max_length=50, )

    class Meta:
        db_table = 'tbl_event_tmp'


class TblSites(models.Model):
    site_id = models.AutoField(primary_key=True)
    site_name = models.CharField(
        max_length=255, )
    site_email = models.CharField(
        max_length=200, )
    site_contact = models.CharField(
        max_length=30, )
    site_address = models.TextField()
    site_status = models.IntegerField()
    client_id = models.IntegerField()
    site_creation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_sites'
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
        unique_together = (('site_name', 'site_email', 'client_id'),)

    def __str__(request):
        return(request.site_name)

class TblStatus(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status_name = models.CharField(
        unique=True, max_length=50, )

    class Meta:
        db_table = 'tbl_status'


class TblSystem(models.Model):
    system_id = models.AutoField(primary_key=True)
    system_name = models.CharField(
        max_length=200, )
    system_ip = models.CharField(
        max_length=30, )
    system_use = models.TextField()
    system_status = models.IntegerField()
    site_id = models.IntegerField()
    system_creation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_system'
        verbose_name = 'System'
        verbose_name_plural = 'Systems'
        unique_together = (('system_name', 'system_ip', 'site_id'),)

    def __str__(request):
        return(request.system_name)

class TblTmpclear(models.Model):
    tmp_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'tbl_tmpclear'

