from .models import BotCommandEntry
from rest_framework import serializers


class BotCommandEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BotCommandEntry
        fields = ('name', 'entry_lang', 'aliases', 'owner_only', 'bot_owner_only',
                  'allows_pm', 'description', 'usage', 'config_help')
