from django.db import models

# Create your models here.

class HostList(mode.model):
    ip = models.CharField(max_length=20, verbose_bame='IP��ַ')
    hostname = models.CharField(max_length=30, verbose_bame='IP������')
    product = models.CharField(max_length=20, verbose_name=u'��Ʒ')
    application = models.CharField(max_length=20, verbose_name=u'Ӧ��')
    idc_jg = models.CharField(max_length=10, blank=True, verbose_name=u'������')
    status = models.CharField(max_length=10, verbose_name=u'ʹ��״̬')
    remark = models.TextField(max_length=50, blank=True, verbose_name=u'��ע')

    def __srt__(self):
        return u'%s - %s - %s' %(self.ip, self.hostname, self.application )

    class Meta:
        verbose_name = u'�����б�'
        verbose_name = u'�����б����'


class ServerAsset(models.Model):
    manufacturer = models.CharField(max_length=20, verbose_name=u'����')
    service_sn = models.CharField(max_length=80, unique=True, verbose_name=u'���к�')
    cpu_model = models.CharField(max_length=50, verbose_name=u'CPU�ͺ�')
    cpu_nums = models.PositiveSmallIntegerField(verbose_name=u'CPU�߳���')
    mem = models.CharField(max_length=5, verbose_name='�ڴ��С')
    disk = models.CharField(max_length=5, verbose_name='Ӳ�̴�С')
    hostname = models.CharField(max_length=30, verbose_name=u'������')
    ip = models.CharField(max_length=20, verbose_name=u'IP��ַ')
    macaddress = models.CharField(max_length=40, verbose_name=u'MAC��ַ')
    os = models.CharField(max_length=20, verbose_name=u'����ϵͳ')
    virtual = models.CharField(max_length=20, verbose_name=u'�Ƿ�Ϊ�����')
    #productname = models.CharField(max_length=30, verbose_name=u'��Ʒ�ͺ�')
    #cpu_groups = models.PositiveSmallIntegerField(verbose_name=u'CPU�������')
    #raid = models.CharField(max_length=5, verbose_name='RAID����')
    #idc_name = models.CharField(max_length=10, blank=True, verbose_name=u'��������')

    def __str__(self):
        return u'%s - %s' %(self.ip, self.hostname )

    class Meta:
        verbose_name = u'�����ʲ���Ϣ'
        verbose_name_plural = u'�����ʲ���Ϣ����'

