from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Careers
from .serializers import CareersSerializers

# Create your views here.
class CareersViewSet(viewsets.ModelViewSet):
    queryset = Careers.objects.all()
    serializer_class = CareersSerializers

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.title = request.data.get('title', instance.title) 
        instance.content = request.data.get('content', instance.content)

        serializer = self.get_serializer(instance, data={
            'title': instance.title, 
            'content': instance.content
        }, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
