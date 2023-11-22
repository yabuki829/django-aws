from django.http import HttpResponse


def index(request):
    return HttpResponse("AWS EC2でこの文字を表示する")