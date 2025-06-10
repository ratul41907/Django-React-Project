from rest_framework import serializers

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Room'  # Assuming 'Room' is defined in the models.py file
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip','created_at')  # Serialize all fields of the Room model