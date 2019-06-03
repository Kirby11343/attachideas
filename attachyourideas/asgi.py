import os
import channels.asgi
from channels.layers import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attachyourideas.settings")
channel_layer = channels.asgi.get_channel_layer()
