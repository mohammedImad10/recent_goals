from rest_framework import serializers
from score_bat_highlights.models import BatHighlight

class BatHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatHighlight
        fields = ('id', 'title', 'competition', 'date', 'embed_video')
