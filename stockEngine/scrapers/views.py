import json
from django.http import HttpResponse, JsonResponse
from scrapers.scrapers import Anue
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
# @authentication_classes((SessionAuthentication, TokenAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def news_detail_api_view(request, stock_no):
    try:
        anue = Anue(stock_no=stock_no)
    except Anue.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        context = anue.scrape()
        return Response(context)