from termcolor import cprint
from discord_webhook import DiscordEmbed, DiscordWebhook

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
    FOOTER = 'Made by jerem.#3609'

    def __init__(self, webhook: DiscordWebhook, color: str = '03a9fc', thumbnail: str = None, footer: str = FOOTER):
        self.webhook = webhook
        self.color = color
        self.thumbnail = thumbnail
        self.footer = footer

    def ItemMetadataUpdated(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Metadata Updated !', color=self.color)

            if name := payload['payload']['item']['metadata'].get('name'):
                embed.add_embed_field(name='Name :', value=str(name))

            if chain_name := payload['payload']['item']['chain'].get('name'):
                embed.add_embed_field(name='Chain :', value=str(chain_name))

            if image_url := payload['payload']['item']['metadata'].get('image_url'):
                embed.set_thumbnail(url=str(image_url))
            elif self.thumbnail:
                embed.set_thumbnail(url=str(self.thumbnail))
            else:
                embed.set_thumbnail(url=str(self.OPENSEA_LOGO_URL))
                
            links = ''
            if metadata_url := payload['payload']['item']['metadata'].get('metadata_url'):
                links += f'[Metadata]({metadata_url}) • '
            if permalink := payload['payload']['item'].get('permalink'):
                links += f'[Asset]({permalink})'

            if links != '':
                embed.add_embed_field(name='Links :', value=str(links), inline=False)
            if self.footer:
                embed.set_footer(text=str(self.footer))
                
            return embed
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def ItemCancelled(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Cancelled !', color=self.color)
            
            if name := payload['payload']['item']['metadata'].get('name'):
                embed.add_embed_field(name='Name :', value=name)

            if base_price := payload['payload'].get('base_price'):
                embed.add_embed_field(name='Price :', value=str(int(base_price)/10**18))
            
            if chain_name := payload['payload']['item']['chain'].get('name'):
                embed.add_embed_field(name='Chain :', value=chain_name)

            if image_url := payload['payload']['item']['metadata'].get('image_url'):
                embed.set_thumbnail(url=image_url)
            elif self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            else:
                embed.set_thumbnail(url=self.OPENSEA_LOGO_URL)
            
            links = ''
            if payload['payload'].get('transaction') and payload['payload']['transaction'].get('hash'):
                hash_ = payload['payload']['transaction']['hash']
                links += f'[Order](https://etherscan.io/tx/{hash_}) • '
            if maker := payload['payload']['maker'].get('address'):
                links += f'[Maker](https://etherscan.io/address/{maker}) • '
            if metadata_url := payload['payload']['item']['metadata'].get('metadata_url'):
                links += f'[Metadata]({metadata_url}) • '
            if permalink := payload['payload']['item'].get('permalink'):
                links += f'[Asset]({permalink})'

            if links != '':
                embed.add_embed_field(name='Links :', value=str(links), inline=False)
            if self.footer:
                embed.set_footer(text=str(self.footer))
                
            return embed
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def ItemListed(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Listed !', color=self.color)
            
            if name := payload['payload']['item']['metadata'].get('name'):
                embed.add_embed_field(name='Name :', value=name)

            if base_price := payload['payload'].get('base_price'):
                embed.add_embed_field(name='Price :', value=str(int(base_price)/10**18))
            
            if chain_name := payload['payload']['item']['chain'].get('name'):
                embed.add_embed_field(name='Chain :', value=chain_name)

            if image_url := payload['payload']['item']['metadata'].get('image_url'):
                embed.set_thumbnail(url=image_url)
            elif self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            else:
                embed.set_thumbnail(url=self.OPENSEA_LOGO_URL)
            
            links = ''
            if maker := payload['payload']['maker'].get('address'):
                links += f'[Maker](https://etherscan.io/address/{maker}) • '
            if metadata_url := payload['payload']['item']['metadata'].get('metadata_url'):
                links += f'[Metadata]({metadata_url}) • '
            if permalink := payload['payload']['item'].get('permalink'):
                links += f'[Asset]({permalink})'

            if links != '':
                embed.add_embed_field(name='Links :', value=str(links), inline=False)
            if self.footer:
                embed.set_footer(text=str(self.footer))

            return embed
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def ItemSold(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Sold !', color=self.color)
            
            if name := payload['payload']['item']['metadata'].get('name'):
                embed.add_embed_field(name='Name :', value=name)

            if sale_price := payload['payload'].get('sale_price'):
                embed.add_embed_field(name='Price :', value=str(int(sale_price)/10**18))
            
            if chain_name := payload['payload']['item']['chain'].get('name'):
                embed.add_embed_field(name='Chain :', value=chain_name)

            if image_url := payload['payload']['item']['metadata'].get('image_url'):
                embed.set_thumbnail(url=image_url)
            elif self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            else:
                embed.set_thumbnail(url=self.OPENSEA_LOGO_URL)
            
            links = ''
            if payload['payload'].get('transaction') and payload['payload']['transaction'].get('hash'):
                hash_ = payload['payload']['transaction']['hash']
                links += f'[Order](https://etherscan.io/tx/{hash_}) • '
            if maker := payload['payload']['maker'].get('address'):
                links += f'[Maker](https://etherscan.io/address/{maker}) • '
            if taker := payload['payload']['taker'].get('address'):
                links += f'[Taker](https://etherscan.io/address/{taker}) • '
            if metadata_url := payload['payload']['item']['metadata'].get('metadata_url'):
                links += f'[Metadata]({metadata_url}) • '
            if permalink := payload['payload']['item'].get('permalink'):
                links += f'[Asset]({permalink})'

            if links != '':
                embed.add_embed_field(name='Links :', value=str(links), inline=False)
            if self.footer:
                embed.set_footer(text=str(self.footer))
                
            return embed
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()
    
    def ItemTransferred(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Transferred !', color=self.color)
            
            if name := payload['payload']['item']['metadata'].get('name'):
                embed.add_embed_field(name='Name :', value=name)

            if sale_price := payload['payload'].get('sale_price'):
                embed.add_embed_field(name='Price :', value=str(int(sale_price)/10**18))
            
            if chain_name := payload['payload']['item']['chain'].get('name'):
                embed.add_embed_field(name='Chain :', value=chain_name)
            
            if quantity := payload['payload'].get('quantity'):
                embed.add_embed_field(name='Quantity :', value=str(quantity))

            if image_url := payload['payload']['item']['metadata'].get('image_url'):
                embed.set_thumbnail(url=image_url)
            elif self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            else:
                embed.set_thumbnail(url=self.OPENSEA_LOGO_URL)
            
            links = ''
            if payload['payload'].get('transaction') and payload['payload']['transaction'].get('hash'):
                hash_ = payload['payload']['transaction']['hash']
                links += f'[Order](https://etherscan.io/tx/{hash_}) • '
            if maker := payload['payload']['from_account'].get('address'):
                links += f'[Maker](https://etherscan.io/address/{maker}) • '
            if taker := payload['payload']['to_account'].get('address'):
                links += f'[Taker](https://etherscan.io/address/{taker}) • '
            if metadata_url := payload['payload']['item']['metadata'].get('metadata_url'):
                links += f'[Metadata]({metadata_url}) • '
            if permalink := payload['payload']['item'].get('permalink'):
                links += f'[Asset]({permalink})'

            if links != '':
                embed.add_embed_field(name='Links :', value=str(links), inline=False)
            if self.footer:
                embed.set_footer(text=str(self.footer))
                
            return embed
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def ItemReceivedOffer(self, payload: dict):
        print(payload)
        try:   
            embed = DiscordEmbed(title='New Item Received Offer !', color=self.color)

            if name := payload['payload']['item']['metadata'].get('name'):
                embed.add_embed_field(name='Name :', value=name)

            if base_price := payload['payload'].get('base_price'):
                embed.add_embed_field(name='Price :', value=str(int(base_price)/10**18))
            
            if chain_name := payload['payload']['item']['chain'].get('name'):
                embed.add_embed_field(name='Chain :', value=chain_name)

            if quantity := payload['payload'].get('quantity'):
                embed.add_embed_field(name='Quantity :', value=str(quantity))

            if image_url := payload['payload']['item']['metadata'].get('image_url'):
                embed.set_thumbnail(url=image_url)
            elif self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            else:
                embed.set_thumbnail(url=self.OPENSEA_LOGO_URL)
            
            links = ''
            if maker := payload['payload']['maker'].get('address'):
                links += f'[Maker](https://etherscan.io/address/{maker}) • '
            if payload['payload'].get('taker') and payload['payload']['taker']['address']:
                taker = payload['payload']['taker']['address']
                links += f'[Taker](https://etherscan.io/address/{taker}) • '
            if metadata_url := payload['payload']['item']['metadata'].get('metadata_url'):
                links += f'[Metadata]({metadata_url}) • '
            if permalink := payload['payload']['item'].get('permalink'):
                links += f'[Asset]({permalink})'

            if links != '':
                embed.add_embed_field(name='Links :', value=str(links), inline=False)
            if self.footer:
                embed.set_footer(text=str(self.footer))
                
            return embed
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def ItemReceivedBid(self, payload: dict):
        try:   
            embed = DiscordEmbed(title='New Item Receive Bid !', color=self.color)

            if name := payload['payload']['item']['metadata'].get('name'):
                embed.add_embed_field(name='Name :', value=name)

            if base_price := payload['payload'].get('base_price'):
                embed.add_embed_field(name='Price :', value=str(int(base_price)/10**18))
            
            if chain_name := payload['payload']['item']['chain'].get('name'):
                embed.add_embed_field(name='Chain :', value=chain_name)

            if quantity := payload['payload'].get('quantity'):
                embed.add_embed_field(name='Quantity :', value=str(quantity))

            if image_url := payload['payload']['item']['metadata'].get('image_url'):
                embed.set_thumbnail(url=image_url)
            elif self.thumbnail:
                embed.set_thumbnail(url=self.thumbnail)
            else:
                embed.set_thumbnail(url=self.OPENSEA_LOGO_URL)
            
            links = ''
            if maker := payload['payload']['maker'].get('address'):
                links += f'[Maker](https://etherscan.io/address/{maker}) • '
            if payload['payload'].get('taker') and payload['payload']['taker']['address']:
                taker = payload['payload']['taker']['address']
                links += f'[Taker](https://etherscan.io/address/{taker}) • '
            if metadata_url := payload['payload']['item']['metadata'].get('metadata_url'):
                links += f'[Metadata]({metadata_url}) • '
            if permalink := payload['payload']['item'].get('permalink'):
                links += f'[Asset]({permalink})'

            if links != '':
                embed.add_embed_field(name='Links :', value=str(links), inline=False)
            if self.footer:
                embed.set_footer(text=str(self.footer))
            return embed
        except Exception as e:
            Logger(f'Failed to build embed {e}').error()

    def send(self, payload: dict):
        try:
            if payload.get('event_type') == EventTypes.ITEM_METADATA_UPDATED:
                embed = self.ItemMetadataUpdated(payload)
            elif payload.get('event_type') == EventTypes.ITEM_CANCELLED:
                embed = self.ItemCancelled(payload)
            elif payload.get('event_type') == EventTypes.ITEM_LISTED:
                embed = self.ItemListed(payload)
            elif payload.get('event_type') == EventTypes.ITEM_SOLD:
                embed = self.ItemSold(payload)
            elif payload.get('event_type') == EventTypes.ITEM_TRANSFERRED:
                embed = self.ItemTransferred(payload)
            elif payload.get('event_type') == EventTypes.ITEM_RECEIVED_OFFER:
                embed = self.ItemReceivedOffer(payload)
            elif payload.get('event_type') == EventTypes.ITEM_RECEIVED_BID:
                embed = self.ItemReceivedBid(payload)
            else:
                Logger('Failed to get event type: ' + str(payload.get('event_type'))).error()
                return 

            self.webhook.remove_embeds()
            self.webhook.add_embed(embed=embed)
            self.webhook.execute()
        except Exception as e:
            Logger(f'Failled to execute webhook : {e}').error()
