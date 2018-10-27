import certifi
import urllib3
import json
import logging
from background_task import background
from discord_cl import settings

logger = logging.getLogger(__name__)
guild_data = None


def get_guild():
    if settings.DISCORD_BOT_SECRET == '' or settings.DISCORD_GUILD_ID == '':
        return None

    url = 'https://discordapp.com/api/v6/guilds/{}'.format(settings.DISCORD_GUILD_ID)
    headers = {
        'User-Agent': 'Bot/Discord.cl (https://discord.cl/, 1.0',
        'Authorization': 'Bot {}'.format(settings.DISCORD_BOT_SECRET)
    }

    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    logger.info('Loading %s ...', url)
    r = http.request('GET', url, headers=headers)
    if r.status == 200:
        data = json.loads(r.data.decode('utf-8'))
        logger.info('Loaded guild information')

        global guild_data
        guild_data = data


@background(schedule=60)
def get_guild_sched():
    get_guild()


def ctx(_):
    if guild_data is None:
        return {}

    return {
        'guild_icon': 'https://cdn.discordapp.com/icons/{guild_id}/{guild_hash}.png'.format(
            guild_id=guild_data['id'],
            guild_hash=guild_data['icon']
        )
    }
