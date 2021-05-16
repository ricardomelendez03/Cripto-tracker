from bs4 import BeautifulSoup
import requests
import schedule


def bot_send_text(bot_message):
    
    bot_token = '1873937761:AAEQHg_JqyqqnZ1mJna1FIjdrf6HG2_FGJc'
    bot_chatID = '1776085993'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def btc_scraping(coin_name):
    url = requests.get('https://awebanalysis.com/es/coin-details/' + coin_name + '/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})
    format_result = result.text

    return format_result


def job():
    comentario = 'Primera versión del tracker, los valores de las principales criptomonedas en el momento son:'
    btc_price = '-- Bitcoin: ' + btc_scraping('bitcoin')
    eth_price = '-- Ethereum: ' + btc_scraping('ethereum')
    bnb_price = '-- Binance Coin: ' + btc_scraping('binance-coin')
    doge_price = '-- DOGE: ' + btc_scraping('dogecoin')   
    bot_send_text(comentario +'\n' + btc_price +'          ' + eth_price + '\n' + bnb_price + '     '+ doge_price)


if __name__ == '__main__':
    job()
    schedule.every(60).minutes.do(job)

    while True:
         schedule.run_pending()