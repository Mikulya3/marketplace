from rest_framework import serializers

from .models import get_data


class ParcingSerializers(serializers.Serializer):
    title = serializers.CharField(required=True)

    def ___str__(self):
        return self.title

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance['title'] != instance['title'].capitalize():
            raise serializers.ValidationError('Название должно быть написано с большой буквы')
        try:
            data = get_data(instance['title'])
        except:
            raise serializers.ValidationError('Название написано неверно')
        rep['calories'] = data['calories']
        rep['jiry'] = data['jiry']
        rep['belki'] = data['belki']
        rep['uglevody'] = data['uglevody']
        rep['voda'] = data['voda']
        rep['zola'] = data['zola']
        return rep