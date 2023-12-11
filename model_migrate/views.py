from django.shortcuts import render

from model_migrate.models import Teacher


def list_pages(request):
    my_dict = {
        'title': 'Список страниц',
    }
    return render(request, 'model_migrate/index.html', my_dict)


def list_school(request):
    list_teacher = Teacher.objects.all()
    my_dict = {
        'school': list_teacher,
        'title': 'Страница школы',
    }
    return render(request, 'model_migrate/school.html', my_dict)


def filter_teacher(request, id_):
    list_teacher = Teacher.objects.filter(id=id_)
    my_dict = {
        'school': list_teacher,
        'title': 'Страница школы',
    }
    return render(request, 'model_migrate/school.html', my_dict)



