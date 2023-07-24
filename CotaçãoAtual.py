import requests

requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_a = requisicao.json()
requisicao_b = requisicao.json()
cotacao_dolar = requisicao_a["USDBRL"]["bid"]
cotacao_euro = requisicao_b["EURBRL"]["bid"]
print(cotacao_dolar)
print(cotacao_euro)
