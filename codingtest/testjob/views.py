from django.db.models import Prefetch

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from testjob.models import Food, FoodCategory
from testjob.serializers import FoodListSerializer


@api_view(["GET"])
def get_food(_):
    foods = Food.objects.filter(is_publish=True)
    categories = FoodCategory.objects.prefetch_related(
        Prefetch(
            'food', queryset=foods
        )
    ).filter(food__is_publish__isnull=False).distinct()

    response_data: list = FoodListSerializer(categories, many=True).data
    return Response(response_data, status=status.HTTP_200_OK)
