from cryptocompy import price
import pprint
value = price.get_current_price(["BTC", "LTC", 'ZEC'], 'EUR')

pprint.pprint(value, width=1)
