from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from openalpr import Alpr

alpr = Alpr("us","/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")

# Create your views here.
@api_view(['POST'])
@parser_classes((MultiPartParser,))
def licence_imgs_list(request):
    if request.method == 'POST':
        img_file = request.FILES['img_file']
        results = alpr.recognize_array(img_file.read())
        return Response(results)

