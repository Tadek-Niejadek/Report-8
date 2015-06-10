from rest_framework import serializers
import models

class post_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.post
		fields = ('id', 'body', 'time')
		
class authpost_serializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.PrimaryKeyRelatedField(
		read_only=True, required=False, allow_null=True, default='0')
	def validate_owner(self,value):
		return self.context['request'].user
		
	class Meta:
		model = models.authpost
		fields = ('id', 'owner', 'body', 'time')
