from scrapers.scrapers import Anue
from rest_framework.views import APIView
from rest_framework import authentication, permissions

def index(request):

    anue = Anue(request.POST.get('stock_no'))

    return JsonResponse(anue.scrape(), safe=False)