# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

# models
from .models import Item

# serializers
from .serializers import ItemSerializer


@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def item_detail(request, pk):
    try:
        item = Item.objects.get(id=pk)
        serializer = ItemSerializer(item, many=False)
        return Response(serializer.data)
    except Item.DoesNotExist:
        return Response('The Item does not exist')


@api_view(['POST'])
def item_create(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def item_update(request, pk):
    try:
        item = Item.objects.get(id=pk)
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Invalid data format')
    except Item.DoesNotExist:
        return Response('The Item does not exist')


@api_view(['DELETE'])
def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response('Item deleted')
