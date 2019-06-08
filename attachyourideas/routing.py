from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path

from homepage.consumers import CommentConsumer

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
        	URLRouter([
        		path('post/<int:pk>/', CommentConsumer)
        		])
        	)
    ),
})

