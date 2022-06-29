from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializers
from .models import Product


@api_view(['GET'])
def test(request):
    dict_ = {
        'str': "hello",
        'int': 12,
        'float': 9.99,
        'bool': True,
        'list': [1, 2, 3]
    }
    return Response(data=dict_, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_detail_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={"error": f"Продукт с id = {id} не существует!!!"})
    data = ProductSerializers(product).data
    return Response(data=data)