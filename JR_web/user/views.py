from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def userView(request):
    cookies = dict(request.COOKIES)
    headers = dict(request.headers)
    post = (request.POST)
    get = (request.GET)
    objects = dict(request.session)
    print(request.user)
    return JsonResponse({'cookies':cookies,'headers':headers,'POST':post,'GET':get,'objects':objects})