# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *

from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
import uuid
import json
import datetime as dt

from django_user_agents.utils import get_user_agent


def add_message(name, phone, email, content):
    message = Message()
    message.name = name
    message.phone = phone
    message.email = email
    message.content = content
    message.save()


def index_view(request):
    lawyer = Lawyer.objects.all().first()
    result = {}
    result['name'] = lawyer.name
    result['image_url'] = lawyer.image.url
    result['description'] = lawyer.description
    menu = "index_menu"

    index_images = IndexImages.objects.all()
    result['index_images'] = index_images

    # user_agent = get_user_agent(request)
    # if user_agent.is_mobile:
    #     return render(request, 'test.html', {})
    # else:
    return render(request, 'index.html', {'result': result, 'menu': menu})

def index_content_view(request):
    index_content_id = request.GET.get('id', '')
    index_content = IndexContent.objects.filter(pk=index_content_id).first()
    result = {}
    result['content'] = index_content.content
    return render(request, 'index_content.html', {'result': result})

def about_us_view(request):
    about_type = request.GET.get('about_type', '')

    menu = "lawyer_menu"
    result = {}
    result['about_type'] = about_type
    if about_type == u'律师个人':
        lawyer = Lawyer.objects.all().first()
        result['name'] = lawyer.name
        result['description'] = lawyer.description
        result['image_url'] = lawyer.image.url
    elif about_type == u'专业团队':
        lawyer_team = LawyerTeam.objects.all().first()
        result['name'] = lawyer_team.name
        result['description'] = lawyer_team.description
    else:
        law_firm = LawFirm.objects.all().first()
        result['name'] = law_firm.name
        result['description'] = law_firm.description
    return render(request, 'about_us.html', {'result': result, 'menu': menu})

def service_view(request):
    service_type = request.GET.get('service_type', '')
    service = LawService.objects.filter(service_type=service_type).first()

    menu = "service_menu"
    result = {}
    result['service_type'] = service_type
    result['service_description'] = service.description
    return render(request, 'service.html', {'result': result, 'menu': menu})

def news_view(request):
    news_type = request.GET.get('news_type', '')
    news_id = request.GET.get('id', '')
    page_num = request.GET.get('page_num', '1')
    page_num = int(page_num)
    news_list = []
    menu = "news_menu"

    if news_type == u'行业动态':
        news_list = IndustryNews.objects.all().order_by("-id")
        if news_id:
            news = IndustryNews.objects.filter(pk=news_id).first()
            return render(request, 'detail.html', {'data': news, 'menu': menu})
    elif news_type == u'法治社会':
        news_list = SociologyNews.objects.all().order_by("-id")
        if news_id:
            news = SociologyNews.objects.filter(pk=news_id).first()
            return render(request, 'detail.html', {'data': news, 'menu': menu})
    else:
        news_list = LawNews.objects.all().order_by("-id")
        if news_id:
            news = LawNews.objects.filter(pk=news_id).first()
            return render(request, 'detail.html', {'data': news, 'menu': menu})

    temp_news_list = []
    index = 1
    for news in news_list:
        temp_news_list.append((index, news))
        index = index + 1

    news_list = temp_news_list

    index = 0
    result_list = []
    single_list = []
    for news in news_list:
        single_list.append(news)
        index = index + 1

        if index % 10 == 0:
            result_list.append(single_list)
            single_list = []

    if index % 10 != 0:
        result_list.append(single_list)

    result = {}
    result['news_type'] = news_type
    result['news_list'] = result_list[page_num - 1]

    page_len = len(result_list)
    page_start = 1
    page_end = page_len
    jump = {}

    if page_num > 2:
        page_start = page_num - 2
    if (page_len - page_num) > 2:
        page_end = page_num + 1

    if page_start > 1:
        jump["left_ellipsis"] = True
    if page_end < page_len:
        jump["right_ellipsis"] = True

    if page_num != 1:
        jump["pre_page"] = True
    if page_num != page_len:
        jump["next_page"] = True

    page_range = range(page_start, page_end + 1)

    return render(request, 'news.html', {'result': result, 'menu': menu, 'page_range': page_range, 'current_page': page_num, 
                                        'jump': jump})

def contact_us_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')

        add_message(name, phone, email, content)
        
    menu = "contact_menu"

    return render(request, 'contact_us.html', {'menu': menu})

def law_list_view(request):
    law_type = request.GET.get('law_type', '')
    law_list = []

    if law_type == u'法律规定':
        legal_provisions_list = LegalProvisions.objects.all()
        law_list = legal_provisions_list
    elif law_type == u'行政法规':
        administrative_regulations_list = AdministrativeRegulations.objects.all()
        law_list = administrative_regulations_list
    elif law_type == u'司法解释':
        judicial_interpretation_list = JudicialInterpretation.objects.all()
        law_list = judicial_interpretation_list
    else:
        other_provisions_list = OtherProvisions.objects.all()
        law_list = other_provisions_list

    index = 0
    result_list = []
    single_list = []
    for law in law_list:
        single_list.append(law)
        index = index + 1

        if index % 5 == 0:
            result_list.append(single_list)
            single_list = []

    if index % 5 != 0:
        result_list.append(single_list)

    menu = "law_menu"
    result = {}
    result['law_type'] = law_type
    result['law_list'] = result_list

    return render(request, 'law_list.html', {'result': result, 'menu': menu})

def success_cases_view(request):
    case_type = request.GET.get('case_type', '')
    case_id = request.GET.get('id', '')
    page_num = request.GET.get('page_num', '1')
    page_num = int(page_num)

    menu = "case_menu"

    if case_type == u'律师案例':
        case_list = LawyerCase.objects.all().order_by('-id')

        if case_id:
            case = LawyerCase.objects.filter(pk=case_id).first()
            return render(request, 'case_detail.html', {'data': case, 'case_type': case_type, 'menu': menu})

    else:
        case_list = ClassicCase.objects.all().order_by('id')

        if case_id:
            case = ClassicCase.objects.filter(pk=case_id).first()
            return render(request, 'case_detail.html', {'data': case, 'case_type': case_type, 'menu': menu})

    temp_case_list = []
    index = 1
    for case in case_list:
        temp_case_list.append((index, case))
        index = index + 1

    case_list = temp_case_list

    index = 0
    result_list = []
    single_list = []
    for case in case_list:
        single_list.append(case)
        index = index + 1

        if index % 10 == 0:
            result_list.append(single_list)
            single_list = []

    if index % 10 != 0:
        result_list.append(single_list)

    result = {}
    result['case_type'] = case_type
    result['case_list'] = result_list[page_num - 1]

    page_len = len(result_list)
    page_start = 1
    page_end = page_len
    jump = {}

    if page_num > 2:
        page_start = page_num - 2
    if (page_len - page_num) > 2:
        page_end = page_num + 1

    if page_start > 1:
        jump["left_ellipsis"] = True
    if page_end < page_len:
        jump["right_ellipsis"] = True

    if page_num != 1:
        jump["pre_page"] = True
    if page_num != page_len:
        jump["next_page"] = True

    page_range = range(page_start, page_end + 1)

    return render(request, 'success_cases.html', {'result': result, 'menu': menu, 'page_range': page_range, 'current_page': page_num, 
                                        'jump': jump})



    # index = 0
    # result_list = []
    # single_list = []
    # for case in case_list:
    #     single_list.append(case)
    #     index = index + 1

    #     if index % 3 == 0:
    #         result_list.append(single_list)
    #         single_list = []

    # if index % 3 != 0:
    #     result_list.append(single_list)

    # result = {}
    # result['case_type'] = case_type
    # result['case_list'] = result_list

    # return render(request, 'success_cases.html', {'result': result, 'menu': menu})


def communications_view(request):
    communications_type = request.GET.get('communications_type', '')
    communications_id = request.GET.get('id', '')
    communications_list = []
    page_num = request.GET.get('page_num', '1')
    page_num = int(page_num)
    menu = "communications_menu"

    if communications_type == u'业务交流':
        communications_list = Business.objects.all().order_by("-id")

        if communications_id:
            communications = Business.objects.filter(pk=communications_id).first()
            return render(request, 'detail.html', {'data': communications, 'menu': menu})
    else:
        communications_list = Activity.objects.all().order_by("-id")

        if communications_id:
            communications = Activity.objects.filter(pk=communications_id).first()
            return render(request, 'detail.html', {'data': communications, 'menu': menu})

    temp_communications_list = []
    index = 1
    for communications in communications_list:
        temp_communications_list.append((index, communications))
        index = index + 1

    communications_list = temp_communications_list

    index = 0
    result_list = []
    single_list = []
    for communications in communications_list:
        single_list.append(communications)
        index = index + 1

        if index % 10 == 0:
            result_list.append(single_list)
            single_list = []

    if index % 10 != 0:
        result_list.append(single_list)

    result = {}
    result['communications_type'] = communications_type
    result['communications_list'] = result_list[page_num - 1]

    page_len = len(result_list)
    page_start = 1
    page_end = page_len
    jump = {}

    if page_num > 2:
        page_start = page_num - 2
    if (page_len - page_num) > 2:
        page_end = page_num + 1

    if page_start > 1:
        jump["left_ellipsis"] = True
    if page_end < page_len:
        jump["right_ellipsis"] = True

    if page_num != 1:
        jump["pre_page"] = True
    if page_num != page_len:
        jump["next_page"] = True

    page_range = range(page_start, page_end + 1)

    return render(request, 'communications.html', {'result': result, 'menu': menu, 'page_range': page_range, 'current_page': page_num, 
                                        'jump': jump})


@csrf_exempt
def upload_image(request, dir_name):
    ##################
    #  kindeditor图片上传返回数据格式说明：
    # {"error": 1, "message": "出错信息"}
    # {"error": 0, "url": "图片地址"}
    ##################
    result = {"error": 1, "message": "上传出错"}
    files = request.FILES.get("imgFile", None)
    if files:
        result =image_upload(files, dir_name)
    return HttpResponse(json.dumps(result), content_type="application/json")

#目录创建
def upload_generation_dir(dir_name):
    today = dt.datetime.today()
    dir_name = dir_name + '/%d/%d/' %(today.year,today.month)
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)
    return dir_name

# 图片上传
def image_upload(files, dir_name):
    #允许上传文件类型
    allow_suffix =['jpg', 'png', 'jpeg', 'gif', 'bmp', 'JPG']
    file_suffix = files.name.split(".")[-1]
    if file_suffix not in allow_suffix:
        return {"error": 1, "message": "图片格式不正确"}
    relative_path_file = upload_generation_dir(dir_name)
    path=os.path.join(settings.MEDIA_ROOT, relative_path_file)
    if not os.path.exists(path): #如果目录不存在创建目录
        os.makedirs(path)
    file_name=str(uuid.uuid1())+"."+file_suffix
    path_file=os.path.join(path, file_name)
    file_url = settings.MEDIA_URL + relative_path_file + file_name
    open(path_file, 'wb').write(files.file.read())
    return {"error": 0, "url": file_url}