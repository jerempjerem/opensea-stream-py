from opensea_sdk import *

def callback(e):
    print(e)

class test():
    def __init__(self, message) -> None:
        self.message = message

    def callback(self, payload):
        print(payload, self.message)

Client = OpenseaStreamClient('a6ba39e5df9c433faf752206cd90059f', Network.MAINNET)
Client.onItemListed('*', test('jahzdezfbzebpfbzeubf').callback)
# Client.onItemSold('shellzorb', callback)

Client.startListening()
