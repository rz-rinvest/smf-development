from binance.client import Client

api_key = "3Cicg8nKHzTVxKPeAbKCw0iCOmnq4qf2oPspxxCQkLjP2yr2RtzIpSIMhSxT0IOs"
api_secret = "yNKHYN8pXnixJkIGpooqAdVPfV2F2VRjxaIvamMm1qRq4tL8AoZ2mDvWjWzqkMXE"

client = Client(api_key, api_secret)

trades = client.get_historical_trades(symbol='BNBBTC')

print(len(trades))
