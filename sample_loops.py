import json
import requests
import pandas as pd

symbols = []
def get_all(sym, i)
    params = {'symbol' : i}
    try:
        c = auth.client_from_token_file(config.token_path, config.api_key)
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Chrome(executable_path="C:/Users/tbrid/Desktop/tda-api/chromedriver.exe") as driver:
            c = auth.client_from_login_flow(
                driver, config.api_key, config.redirect_uri, config.token_path)
                
    r = c.get_price_history(f'{i}',
            period_type=client.Client.PriceHistory.PeriodType.YEAR,
            period=client.Client.PriceHistory.Period.TWENTY_YEARS,
            frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
            frequency=client.Client.PriceHistory.Frequency.DAILY)
    if r.status_code == 200:
        res = json.loads(r.text)
    else:
        raise Exception(f'API error with status code {r.status_code}')
    return res
responses = pd.DataFrame([get_all(sym, i) for i in symbols])
    # print(json.dumps(r.json(), indent=4))


# def get_data(endpoint, i):
#     api_endpoint = endpoint
#     params = {'customerid' : i}
#     response = requests.get(f"{API_BASEURL}/{api_endpoint}",
#                          params = params,
#                          headers = HEADERS)
#     if response.status_code == 200:
#         res = json.loads(response.text)
#     else:
#         raise Exception(f'API error with status code {response.status_code}')

#     return res

# responses = pd.DataFrame([get_data(endpoint, i) for i in customerlist])
get_all(symbols)