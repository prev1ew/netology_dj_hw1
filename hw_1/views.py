from django.shortcuts import render
from nt_dj_1.settings import BASE_DIR


def index(request):
    return render(request, 'hw_1/index.html')


def work_dir(request):
    content = {
        'path': BASE_DIR
    }
    return render(request, 'hw_1/work_dir.html', content)


def current_time(request):
    return render(request, 'hw_1/current_time.html')
