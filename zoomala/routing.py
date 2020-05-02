from django.conf.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from chat.consumers import ChatConsumer
application = ProtocolTypeRouter({ 
    # Websocket chat handler
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    #url(r"chat/", ChatConsumer, name='chat')
                    re_path(r"messages/(?P<username>[\w.@+-]+)", ChatConsumer, name='chat')
                ]
            )
        ),
    )
})