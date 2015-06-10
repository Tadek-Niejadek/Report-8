import models
from rest_framework import viewsets
import serializers

class post(viewsets.ModelViewSet):
	serializer_class = serializers.post_serializer
	queryset = models.post.objects.all()
	#def get_queryset(request):
	
"""	def get(self, request):
		posts = post.objects.all()
		serializer = post_serializer(posts, many=True)
		#return Response(serializer.data)

	def post(self, request):
		serializer = post_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""
	
class authpost(viewsets.ModelViewSet):
	serializer_class = serializers.authpost_serializer
	queryset = models.authpost.objects.all()
