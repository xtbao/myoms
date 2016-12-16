#coding:utf-8
from django.db import models

# Create your models here.

class Idc(models.Model):
    idc_name = models.CharField(max_length=40, verbose_name='机房名称')
    remark = models.CharField(max_length=40, verbose_name='备注')

    def __unicode__(self):
        return self.idc_name
    class Meta:
        verbose_name = '机房列表'
        verbose_name_plural = '机房列表'


class HostList(models.Model):
    ip = models.GenericIPAddressField(unique=True, verbose_name='IP地址')
    hostname = models.CharField(max_length=30, verbose_name='主机名')
    #group = models.ManyToManyField('Group', null=True, blank=True ,verbose_name='组名')
    group = models.ManyToManyField('Group', blank=True ,verbose_name='组名')
    application = models.CharField(max_length=20, verbose_name='应用')
    bianhao = models.CharField(max_length=30, verbose_name='编号')
    idc_name = models.CharField(max_length=40,null=True,blank=True, verbose_name='所属机房')

    def __unicode__(self):
        return self.ip
    class Meta:
        verbose_name = '主机列表'
        verbose_name_plural = '主机列表'

class ServerAsset(models.Model):
    manufacturer = models.CharField(max_length=20, verbose_name='厂商')
    service_sn = models.CharField(max_length=80, unique=True, verbose_name='序列号')
    cpu_model = models.CharField(max_length=50, verbose_name='CPU型号')
    cpu_nums = models.PositiveSmallIntegerField(verbose_name='CPU线程数')
    mem = models.CharField(max_length=5, verbose_name='内存大小')
    disk = models.CharField(max_length=5, verbose_name='硬盘大小')
    hostname = models.CharField(max_length=30, verbose_name='主机名')
    ip = models.CharField(max_length=20, verbose_name='IP地址')
    macaddress = models.CharField(max_length=40, verbose_name='MAC地址')
    os = models.CharField(max_length=20, verbose_name='操作系统')
    virtual = models.CharField(max_length=20, verbose_name='是否为虚拟机')
    #productname = models.CharField(max_length=30, verbose_name=u'产品型号')
    #cpu_groups = models.PositiveSmallIntegerField(verbose_name=u'CPU物理核数')
    #raid = models.CharField(max_length=5, verbose_name='RAID级别')
    #idc_name = models.CharField(max_length=10, blank=True, verbose_name=u'所属机房')

    def __unicode__(self):
        return '%s - %s' %(self.ip, self.hostname )

    class Meta:
        verbose_name = '主机资产信息'
        verbose_name_plural = '主机资产信息管理'

class Group(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'主机组信息'
        verbose_name_plural = u'主机组信息管理'
