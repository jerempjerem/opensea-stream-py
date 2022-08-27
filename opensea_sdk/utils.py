from turtle import color
from termcolor import cprint
from discord_webhook import DiscordEmbed, DiscordWebhook
import datetime

class Network():
    MAINNET : str = "wss://stream.openseabeta.com/socket/websocket"
    TESTNET : str = "wss://testnets-stream.openseabeta.com/socket/websocket"

class EventTypes():
    ITEM_METADATA_UPDATED: str = 'item_metadata_updated'
    ITEM_LISTED : str = 'item_listed'
    ITEM_SOLD : str = 'item_sold'
    ITEM_TRANSFERRED : str = 'item_transferred'
    ITEM_RECEIVED_OFFER : str = 'item_received_offer'
    ITEM_RECEIVED_BID : str = 'item_received_bid'
    ITEM_CANCELLED : str = 'item_cancelled'

class Logger():
    def __init__(self, message: str) -> None:
        self.message = message

    def debug(self):
        cprint(f'[DEBUG]: {self.message}', 'cyan')

    def info(self):
        cprint(f'[INFO]: {self.message}', 'green')

    def warn(self):
        cprint(f'[WARN]: {self.message}', 'yellow')

    def error(self):
        cprint(f'[ERROR]: {self.message}', 'red')

class Webhook():

    OPENSEA_LOGO_URL = 'https://pbs.twimg.com/profile_images/1544105652330631168/ZuvjfGkT_400x400.png'
    FOOTER = 'Made by jerem.#3609 | ' + str(datetime.datetime.utcnow()).split('.')[0]

    def __init__(self, webhook: DiscordWebhook, color: str = '03a9fc', thumbnail: str = OPENSEA_LOGO_URL, footer: str = FOOTER):
        self.webhook = webhook
        self.color = color
        self.thumbnail = thumbnail
        self.footer = footer

    def ItemMetadataUpdated(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Metadata Updated !', color=self.color)
            
            if self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            if self.footer:
                embed.set_footer(text=self.footer)

            if self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            if self.footer:
                embed.set_footer(text=self.footer)
                
            self.send(embed)
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def ItemCancelled(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Cancelled !', color=self.color)
            if self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            if self.footer:
                embed.set_footer(text=self.footer)
                
            self.send(embed)
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def ItemListed(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Listed !', color=self.color)
            if self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            if self.footer:
                embed.set_footer(text=self.footer)
                
            self.send(embed)
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def ItemSold(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Sold !', color=self.color)
            if self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            if self.footer:
                embed.set_footer(text=self.footer)
                
            self.send(embed)
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()
    
    def ItemTransferred(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Transferred !', color=self.color)
            embed.set
            if self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            if self.footer:
                embed.set_footer(text=self.footer)
                
            self.send(embed)
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def ItemReceivedOffer(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Received Offer !', color=self.color)
            if self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            if self.footer:
                embed.set_footer(text=self.footer)
                
            self.send(embed)
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def ItemReceivedBid(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Receive Bid !', color=self.color)
            if self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            if self.footer:
                embed.set_footer(text=self.footer)
                
            self.send(embed)
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def send(self, embed: DiscordEmbed):
        try:
            self.webhook.remove_embeds()
            self.webhook.add_embed(embed=embed)
            self.webhook.execute()
        except Exception as e:
            Logger(f'Failled to execute webhook : {e}').error()
