# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

from datetime import datetime
import pytz


@admin.register(IndexImages)
class IndexImagesAdmin(admin.ModelAdmin):
    pass


# Lawyer Module
@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/description_config.js',
        )

@admin.register(LawyerTeam)
class LawyerTeamAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/description_config.js',
        )



# Law Service
@admin.register(LawService)
class LawServiceAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/description_config.js',
        )


# Success Cases
@admin.register(LawyerCase)
class LawyerCaseAdmin(admin.ModelAdmin):
    list_display = ('title',)

    class Media:
        js = (
            'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/config.js',
        )

@admin.register(ClassicCase)
class ClassicCaseAdmin(admin.ModelAdmin):
    list_display = ('title',)

    class Media:
        js = (
            'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/config.js',
        )


# Law Module
@admin.register(LegalProvisions)
class LegalProvisionsAdmin(admin.ModelAdmin):
    pass

@admin.register(AdministrativeRegulations)
class AdministrativeRegulationsAdmin(admin.ModelAdmin):
    pass

@admin.register(JudicialInterpretation)
class JudicialInterpretationAdmin(admin.ModelAdmin):
    pass

@admin.register(OtherProvisions)
class OtherProvisionsAdmin(admin.ModelAdmin):
    pass


# Law News
@admin.register(IndustryNews)
class IndustryNewsAdmin(admin.ModelAdmin):
    list_display = ('title','submit_time',)

    class Media:
        js = (
            'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/config.js',
        )

@admin.register(SociologyNews)
class SociologyNewsAdmin(admin.ModelAdmin):
    list_display = ('title','submit_time',)

    class Media:
        js = (
            'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/config.js',
        )

@admin.register(LawNews)
class LawNewsAdmin(admin.ModelAdmin):
    list_display = ('title','submit_time',)

    class Media:
        js = (
            'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/config.js',
        )


# Lawyers Communications
@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('title','submit_time',)

    class Media:
        js = (
            'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/config.js',
        )

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title','submit_time',)

    class Media:
        js = (
            'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/config.js',
        )


# Message Module
def display_message(obj):
    return ("%s..." % (obj.content[:20]))

# def submit_time(obj):
#     datetime.fromtimestamp(0, pytz.timezone('Asia/Shanghai'))
#     return "%s" % obj.submit_time.strftime('%Y-%m-%d %H:%M:%S')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', display_message, 'submit_time', 'has_reply',)