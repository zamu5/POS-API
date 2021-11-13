# rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.db import transaction

# models
from .models import Order
from Menu.models import Item

# serializers
from .serializers import OrderSerializer


@transaction.atomic()
def validate_items(items_list):
    err = []
    amount = 0
    for item in items_list:
        try:
            item_id = item.get('id', None)
            quantity = item.get('quantity', None)
            item_obj = Item.objects.get(id=item_id)
            if quantity > item_obj.quantity:
                err.append(
                    f'The Item {item_id} does not have the enough quantity,'
                    f' there are only {item_obj.quantity} available'
                )
                continue
            else:
                item_obj.quantity -= quantity
                item_obj.save()
                amount += item_obj.price * quantity
        except Item.DoesNotExist:
            err.append(f'The Item {item_id} does not exist')

    if err:
        raise Exception(','.join(err))
    return amount


class CreateOrder(APIView):
    def post(self, request):
        data = request.data
        try:
            amount = validate_items(data['items'])
            note = data.get('note', '')
            order = Order.objects.create(
                items=data['items'],
                payment_amount=amount,
                note=note
            )
            return Response(f'Order {order.id} created')
        except Exception as err:
            return Response(str(err))


@api_view(['GET'])
def order_list(request):
    items = Order.objects.all()
    serializer = OrderSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def order_detail(request, pk):
    try:
        item = Order.objects.get(id=pk)
        serializer = OrderSerializer(item, many=False)
        return Response(serializer.data)
    except Item.DoesNotExist:
        return Response('The Order does not exist')

