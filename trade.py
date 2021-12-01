import tda
from tda import auth, client
import json
import config

# token_path = 'token'
# api_key = 'YOUR_API_KEY@AMER.OAUTHAP'
# redirect_uri = 'https://localhost'

# what is our tradeable stock universe
stock_list = []

# example list [aapl, abb, aap, aame, aaic..........]
# example api call iteration for all assets
# for symbol in symbol_list
#   return symbol



try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path="C:/Users/tbrid/Desktop/tda-api/chromedriver.exe") as driver:
        c = auth.client_from_login_flow(
            driver, config.api_key, config.redirect_uri, config.token_path)

r = c.get_price_history('AAPL',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
assert r.status_code == 200, r.raise_for_status()
print(json.dumps(r.json(), indent=4))