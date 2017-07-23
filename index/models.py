# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class IndexContent(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name="标题")
    content = models.TextField(blank=True, verbose_name="内容")

    def __unicode__(self):
        return u'%s' % self.title

class IndexImages(models.Model):
    image = models.ImageField(upload_to="images/", blank=True, verbose_name="图片")
    url = models.CharField(max_length=255, blank=True, verbose_name="链接")
    index_content = models.ForeignKey(IndexContent, null=True, blank=True, verbose_name="对应内容(若存在链接，则以链接为主)")

    def __unicode__(self):
        return u'%s' % self.image


# Lawyer Module
class Lawyer(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    phone = models.CharField(max_length=20, blank=True, verbose_name="联系电话")
    qq = models.CharField(max_length=50, blank=True, verbose_name="QQ")
    address = models.CharField(max_length=100, blank=True, verbose_name="联系地址")
    company = models.CharField(max_length=100, blank=True, verbose_name="公司")
    description = models.TextField(verbose_name="个人简介")
    image = models.ImageField(upload_to="photo/", blank=True, verbose_name="个人照片")

    def __unicode__(self):
        return u'%s' % self.name

class LawyerTeam(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name="团队名称")
    description = models.TextField(blank=True, verbose_name="团队简介")

    def __unicode__(self):
        return u'%s' % self.name

class LawFirm(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name="律所名称")
    description = models.TextField(blank=True, verbose_name="律所简介")

    def __unicode__(self):
        return u'%s' % self.name


# Law Service
class LawService(models.Model):
    service_type = models.CharField(max_length=20, choices=((u'诉讼业务',u'诉讼业务'),(u'非诉业务',u'非诉业务'),(u'委托流程',u'委托流程')), verbose_name="服务类型")
    description = models.TextField(blank=True, verbose_name="服务介绍")

    def __unicode__(self):
        return u'%s' % self.service_type


# Success Cases
class Case(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name="标题")
    # image = models.ImageField(upload_to="photo/", blank=True, verbose_name="案例图片")
    content = models.TextField(verbose_name="内容")

    class Meta:
        abstract = True

class LawyerCase(Case):

    def __unicode__(self):
        return u'%s' % self.title

class ClassicCase(Case):

    def __unicode__(self):
        return u'%s' % self.title


# Law Module
class LawsBaseModel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description_file = models.FileField(upload_to="file/", blank=True, verbose_name="描述文件")

    class Meta:
        abstract = True

class LegalProvisions(LawsBaseModel):

    def __unicode__(self):
        return u'%s' % self.name

class AdministrativeRegulations(LawsBaseModel):

    def __unicode__(self):
        return u'%s' % self.name

class JudicialInterpretation(LawsBaseModel):

    def __unicode__(self):
        return u'%s' % self.name

class OtherProvisions(LawsBaseModel):

    def __unicode__(self):
        return u'%s' % self.name


class Article(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    submit_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Law News
class IndustryNews(Article):

    def __unicode__(self):
        return u'%s' % self.title

class SociologyNews(Article):

    def __unicode__(self):
        return u'%s' % self.title

class LawNews(Article):

    def __unicode__(self):
        return u'%s' % self.title


# Lawyers Communications
class Business(Article):

    def __unicode__(self):
        return u'%s' % self.title

class Activity(Article):

    def __unicode__(self):
        return u'%s' % self.title


# Message Module
class Message(models.Model):
    name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=50, blank=True)
    content = models.CharField(max_length=500, blank=True)
    submit_time = models.DateTimeField(auto_now=True)
    has_reply = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.name


LegalProvisions._meta.get_field('name').verbose_name = "法律规定"
AdministrativeRegulations._meta.get_field('name').verbose_name = "行政法规"
JudicialInterpretation._meta.get_field('name').verbose_name = "司法解释"
OtherProvisions._meta.get_field('name').verbose_name = "其他规定"