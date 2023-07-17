from api.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import ProductSerializer 
from django.views.decorators.csrf import csrf_exempt


@api_view(["GET"])
def get_product_list(request):
    all_products = Product.objects.all()
    serializer = ProductSerializer(all_products, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def add_product(request):
    data = request.data
    instance = ProductSerializer(data=data)
    if instance.is_valid():
        instance.save()
        return Response(instance.data, status=201)
    return Response(instance.errors, status=400) 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import ProductSerializer 

@api_view(['PUT', 'DELETE', 'PATCH'])
def product_changes(request, pk):
    try:
        instance = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"message": "invalid primary key"}, status=400)
    if request.method == "PUT" or request.method=="PATCH":
        part_bool = (request.method == 'PATCH')
        serializer = ProductSerializer(instance, data=request.data, partial=part_bool)
        if not serializer.is_valid():
            return Response({"message": "invalid data"}, status=400)
        serializer.save()
        return Response(serializer.data, status=201)

    if request.method == "DELETE":
        instance.delete()
        return Response(status=204)


        



 