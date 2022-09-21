from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Category
from main.serializers import CategoryAllSerializer, CategoryListSerializer, CategoryCreateSerializer


class HomeApi(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryAllSerializer(categories, many=True)
        print(serializer.data)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

def home(request):
    category=Category.objects.all()
    return render(request, 'index.html', context={'category':category})

class CategoryViewSet(APIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategoryAllSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            try:
                instance = self.queryset.get(id=pk)
                serializer = self.serializer_class(instance)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response(data={'ERROR': 'by given pk object not found!'},
                                status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        serializer = CategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        s = CategoryListSerializer(instance)
        return Response(data=s.data, status=status.HTTP_201_CREATED)




