from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import infoserializer
from .models import vinfo



# Create your views here.


@csrf_exempt
def feedbackform(request):
    if request.method =='POST':
        data1 = JSONParser().parse(request)
        outdata = infoserializer(data=data1)

        if outdata.is_valid():
            outdata.save()
            return JsonResponse(outdata.data, safe=False)
        else:
            return JsonResponse(outdata.errors, safe=False)

    elif request.method == 'GET':
        data = vinfo.objects.all()[:6]
        output = infoserializer(data, many=True)
        return JsonResponse(output.data, safe=False)
