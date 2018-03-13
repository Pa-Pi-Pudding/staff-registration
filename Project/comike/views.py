from django.shortcuts import render
from comike.models import StaffData, Information, Weather
from django.views.decorators.csrf import csrf_protect
from comike.forms import StaffDataForm, InformationForm, WeatherForm


class TemporarilySaved(object):
    staff_name = ""
    staff_name_kana = ""
    gender = ""
    birth_day = ""
    mail_addressttp = ""
    phone_number = ""
    post_code = ""
    address = ""
    e_name = ""
    e_relationship = ""
    e_phone_number = ""
    join_day_0 = ""
    join_day_1 = ""
    join_day_2 = ""
    join_day_3 = ""
    assignment_1 = ""
    assignment_2 = ""
    partner = ""
    parking = ""
    hotel = ""
    password = ""
    memo = ""
    created_date = ""
    updated_date = ""


def entry(request):

    form = StaffDataForm(None)

    return render(request, 'comiket-entry/entry.html', {'form': form, })


@csrf_protect
def confirmation(request):  # 確認をするメソッド
    from copy import deepcopy
    from pprint import pprint

    temp_data = TemporarilySaved()

    if request.method == 'POST':

        form = StaffDataForm(request.POST or None)
        if form.is_valid():

            data = deepcopy(form.cleaned_data)

            temp_data.staff_name = data.get('staff_name', '')
            temp_data.staff_name_kana = data.get('staff_name_kana', '')
            temp_data.gender = data.get('gender', None) or None
            temp_data.birth_day = data.get('birth_day', None) or None
            temp_data.mail_address = data.get('mail_address', '')
            temp_data.phone_number = data.get('phone_number', '')
            temp_data.post_code = data.get('post_code', '')
            temp_data.address = data.get('address', '')
            temp_data.e_name = data.get('e_name', '')
            temp_data.e_relationship = data.get('e_relationship', '')
            temp_data.e_phone_number = data.get('e_phone_number', '')
            temp_data.join_day_0 = data.get('join_day_0', False) or False
            temp_data.join_day_1 = data.get('join_day_1', False) or False
            temp_data.join_day_2 = data.get('join_day_2', False) or False
            temp_data.join_day_3 = data.get('join_day_3', False) or False
            temp_data.assignment_1 = data.get('assignment_1', None) or None
            temp_data.assignment_2 = data.get('assignment_2', None) or None
            temp_data.partner = data.get('partner', '')
            temp_data.parking = data.get('parking', 0) or 0
            temp_data.hotel = data.get('hotel', 0) or 0
            temp_data.password = data.get('password', '')
            temp_data.memo = data.get('memo', '')

            data["birth_day"] = data["birth_day"].strftime("%Y-%m-%d") if data["birth_day"] else ""

            request.session["data"] = data  # sessionでHTTP間で一定時間までデータ共有

            pprint(request.session["data"])

        else:

            print(form.errors)

            return render(request, 'comiket-entry/entry.html', {'form': form, })

    return render(request, 'comiket-entry/confirmation.html', {"data": temp_data})


@csrf_protect
def complete(request):  # DBに送信
    if request.method == 'POST':
        data = request.session.get("data", None)
        if data:
            model = StaffData.objects.create(
                staff_name=data.get('staff_name', ''),
                staff_name_kana=data.get('staff_name_kana', ''),
                gender=data.get('gender', None) or None,
                birth_day=data.get('birth_day', None) or None,
                mail_address=data.get('mail_address', ''),
                phone_number=data.get('phone_number', ''),
                post_code=data.get('post_code', ''),
                address=data.get('address', ''),
                e_name=data.get('e_name', ''),
                e_relationship=data.get('e_relationship', ''),
                e_phone_number=data.get('e_phone_number', ''),
                join_day_0=data.get('join_day_0', False) or False,
                join_day_1=data.get('join_day_1', False) or False,
                join_day_2=data.get('join_day_2', False) or False,
                join_day_3=data.get('join_day_3', False) or False,
                assignment_1=data.get('assignment_1', None) or None,
                assignment_2=data.get('assignment_2', None) or None,
                partner=data.get('partner', ''),
                parking=data.get('parking', 0) or 0,
                hotel=data.get('hotel', 0) or 0,
                password=data.get('password', ''),
                memo=data.get('memo', ''),
            )

    return render(request, 'main-menu/executive.html', {})


def executive(request):
    data = Information.objects.filter().all()
    print(data)
    context = {
        "data": data,
    }
    return render(request, 'main-menu/executive.html', context)


@csrf_protect
def information(request):
    info = InformationForm(None)
    weather = WeatherForm(None)
    data = Information.objects.filter().all()
    context = {
        'info': info,
        'weather': weather,
        'data': data,
    }

    if request.method == 'POST':
        if "information_submit" in request.POST:
            info = InformationForm(request.POST or None)

            if info.is_valid():
                info_data = info.cleaned_data
                model = Information.objects.create(
                    organization=info_data.get('organization', 0)or 0,
                    content=info_data.get('content', ''),
                    title=info_data.get('title', ''),
                )
                model.save()

        elif "weather_submit" in request.POST:
            weather = WeatherForm(request.POST or None)

            if weather.is_valid():
                weather_data = weather.cleaned_data
                model = Weather.objects.create(
                    carrier_shift=weather_data.get('carrier_shift', 0) or 0,
                )
                model.save()

    return render(request, 'main-menu/information-setting.html', context)
