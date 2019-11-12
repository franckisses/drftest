from utils.models import BaseModel
from django.db import models
# Create your models here.

class CompanyInfo(BaseModel):
    company = models.CharField(max_length=100,unique=True,verbose_name=u'公司名')
    email = models.CharField(max_length=200,verbose_name=u'邮箱名')
    start_time = models.DateTimeField(verbose_name=u'生效时间')
    end_time = models.DateTimeField(verbose_name=u'终止时间')
    is_alive = models.BooleanField(default=True,verbose_name=u'是否在有效期')

     # 对当前表进行相关设置: 
    class Meta:
        db_table = 'company'
        verbose_name = '企业信息'
        verbose_name_plural = verbose_name

    # 在 str 魔法方法中, 返回用户名称
    def __str__(self):
        return self.company

class Record(BaseModel):
    company_id = models.ForeignKey('CompanyInfo',verbose_name=u'企业ID')
    season = models.CharField(max_length=5,verbose_name=u'季度')
    send_status = models.BooleanField(default=True,verbose_name=u'发送状态')

    class Meta:
        db_table = 'record'
        verbose_name = '发送记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company_id

