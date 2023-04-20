import openai
import requests
import json
import streamlit as st


# 25 free request of ChatGPT

def BasicGeneration(userPrompt):
    url = "https://simple-chatgpt-api.p.rapidapi.com/ask"

    payload = {"question": userPrompt}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "4234a1b884msh65b86b953831e97p186275jsn3e034269ba5f",
        "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return json.loads(response.text)['answer']


# Free liftime but limited words

# def BasicGeneration(userPrompt):
#     url = "https://chatgpt-api7.p.rapidapi.com/ask"

#     payload = {"query": userPrompt}
#     headers = {
#         "content-type": "application/json",
#         "X-RapidAPI-Key": "4234a1b884msh65b86b953831e97p186275jsn3e034269ba5f",
#         "X-RapidAPI-Host": "chatgpt-api7.p.rapidapi.com"
#     }

#     response = requests.request("POST", url, json=payload, headers=headers)

#     return json.loads(response.text)['response']


def GetCoinPrices(UUID):
	# Define the API endpoint and query parameters
    url = f'https://coinranking1.p.rapidapi.com/coin/{UUID}/history'

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}
	# Define the request headers with API key and host
    headers = {
        "X-RapidAPI-Key": "4234a1b884msh65b86b953831e97p186275jsn3e034269ba5f",
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }
	# Send a GET request to the API endpoint with query parameters and headers
    response = requests.request("GET", url, headers=headers, params=querystring)
    # Parse the response data as a JSON object
    JSONResult = json.loads(response.text)
    # Extract the "history" field from the JSON response
    history = JSONResult["data"]["history"]
    # Extract the "price" field from each element in the "history" array and add to a list
    prices = []
    for change in history:
        prices.append(change["price"])
    # Join the list of prices into a comma-separated string
    pricesList = ','.join(prices)
    # Return the comma-separated string of prices
    return pricesList



st.title('CryptoCurrency Analyzer With ChatGPT')
st.subheader('Made by Abdul Rahman Memon')


option = st.selectbox(
     'Which coin you want to Analyze',
     ('Bitcoin (BTC)', 'Ethereum (ETH)', 'Binance Coin (BNB)', 'Dogecoin (DOGE)', 'XRP (XRP)', 'Cardano (ADA)', 'Polkadot (DOT)', 'Chainlink (LINK)', 'Litecoin (LTC)', 'Stellar (XLM)'))



UUIDs = {
    'Bitcoin (BTC)': 'Qwsogvtv82FCd',
    'Ethereum (ETH)': 'razxDUgYGNAdQ',
    'Binance Coin (BNB)': 'WcwrkfNI4FUAe',
    'Dogecoin (DOGE)': 'a91GCGd_u96cF',
    'XRP (XRP)': '-l8Mn2pVlRs-p',
    'Cardano (ADA)': 'qzawljRxB5bYu',
    'Polkadot (DOT)': '25W7FG7om',
    'Chainlink (LINK)': 'VLqpJwogdhHNb',
    'Litecoin (LTC)': 'D7B1x_ks7WhV5',
    'Stellar (XLM)': 'f3iaFeCKEmkaZ'
}
st.write('You selected:', option, "with UUID:", UUIDs[option])

# Qwsogvtv82FCd
# razxDUgYGNAdQ
# WcwrkfNI4FUAe
# a91GCGd_u96cF
# -l8Mn2pVlRs-p
# qzawljRxB5bYu
# 25W7FG7om
# VLqpJwogdhHNb
# D7B1x_ks7WhV5
# f3iaFeCKEmkaZ


if st.button('Analyze'):
    with st.spinner(f'Getting {option} Prices...'):
        coinPrices = GetCoinPrices(UUIDs[option])
        st.success('Done!')
    with st.spinner(f'Analyzing {option} Prices...'):
        chatGPTPrompt = f"""You are an expert crypto trader with more than 10 years of experience, 
                    I will provide you with a list of {option} prices for the last 7 days
                    can you provide me with a technical analysis
                    of {option} based on these prices. here is what I want: 
                    Price Overview, 
                    Moving Averages, 
                    Relative Strength Index (RSI),
                    Moving Average Convergence Divergence (MACD),
                    Advice and Suggestion,
                    Do I buy or sell?
                    Please be as detailed as much as you can, and explain in a way any beginner can understand. and make sure to use headings
                    Here is the price list: {coinPrices}"""
    
        analysis = BasicGeneration(chatGPTPrompt)
        st.text_area("Analysis", analysis,
                     height=500)
        st.success('Done!')
