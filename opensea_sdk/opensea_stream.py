from realtime.connection import Socket
from realtime.channel import Channel
from .utils import *
from discord_webhook import DiscordWebhook

class OpenseaStreamClient():
    def __init__(self, api_key: str, network: Network = Network.MAINNET):
        socketUrl = f'{network}?token={api_key}'
        self.socket = Socket(socketUrl)

        self.connected = False
        
    def connect(self):
        try:
            Logger('Connecting to socket').debug()
            self.socket.connect()
        except Exception as e:
            Logger(f'Failed to connect to socket : {e}').error()
    
    def createChannel(self, collection_slug: str):
        try:
            channel : Channel = self.socket.set_channel(f'collection:{collection_slug}')
            channel.join()
            Logger(f'Successfully joined channel {collection_slug}').info()
            return channel
        except Exception as e:
            Logger(f'Failed to join channel : {e}').error()

    def getChannels(self, collection_slug: str):
        try:
            if collection_slug not in list(self.socket.channels):
                Logger(f'Creating channel for topic: {collection_slug}').debug()
                return self.createChannel(collection_slug)
            Logger(f'Channel for topic: {collection_slug} already exist').warn()
        except Exception as e:
            Logger(f'Failed to create channel for topic {collection_slug} : {e}').error()

    def on(self, event_type: EventTypes, collection_slug: str, callback):
        try:
            if not self.connected:
                self.socket.connect()
                self.connected = True
            channel = self.getChannels(collection_slug)
            Logger(f'Subscribing to {event_type} events on {collection_slug}').info()
            channel.on(event_type, callback)
        except Exception as e:
            Logger(e).error()

    def startListening(self):
        try:
            Logger(f'Channel joined : {list(self.socket.channels)}').info()
            Logger('Listenning').warn()
            self.socket.listen()
        except Exception as e:
            Logger(e).error()

    def onItemMetadataUpdated(self, collection_slug: str, callback):
        try:
            Logger(f"Listening for item metadata updates on {collection_slug}").debug()
            return self.on(EventTypes.ITEM_METADATA_UPDATED, collection_slug, callback)
        except Exception as e:
            Logger(e).error()

    def onItemCancelled(self, collection_slug: str, callback):
        try:
            Logger(f"Listening for item cancellations on {collection_slug}").debug()
            return self.on(EventTypes.ITEM_CANCELLED, collection_slug, callback)
        except Exception as e:
            Logger(e).error()

    def onItemListed(self, collection_slug: str, callback):
        try:
            Logger(f"Listening for item listings on {collection_slug}").debug()
            return self.on(EventTypes.ITEM_LISTED, collection_slug, callback)
        except Exception as e:
            Logger(e).error()
    
    def onItemSold(self, collection_slug: str, callback):
        try:
            Logger(f"Listening for item sales on {collection_slug}").debug()
            return self.on(EventTypes.ITEM_SOLD, collection_slug, callback)
        except Exception as e:
            Logger(e).error()

    def onItemTransferred(self, collection_slug: str, callback):
        try:
            Logger(f"Listening for item transfers on {collection_slug}").debug()
            return self.on(EventTypes.ITEM_TRANSFERRED, collection_slug, callback)
        except Exception as e:
            Logger(e).error()

    def onItemReceivedOffer(self, collection_slug: str, callback):
        try:
            Logger(f"Listening for item offers on {collection_slug}").debug()
            return self.on(EventTypes.ITEM_RECEIVED_OFFER, collection_slug, callback)
        except Exception as e:
            Logger(e).error()

    def onItemReceivedBid(self, collection_slug: str, callback):
        try:
            Logger(f"Listening for item offers on {collection_slug}").debug()
            return self.on(EventTypes.ITEM_RECEIVED_BID, collection_slug, callback)
        except Exception as e:
            Logger(e).error()