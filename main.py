import pandas as pd
import requests
import json


sites = pd.read_csv('Lista_sites.csv')['Sites'].tolist()


def urlscan(site):
    headers = {'API-Key': 'c18387fb-4ace-44f4-b88a-dee47f067574',
               'Content-Type': 'application/json'}
    data = {"url": f"{site}", "visibility": "private"}
    response = requests.post(
        'https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))

    return response, response.json()


def get_code(response):
    code = list(response)[0]
    response_code = str(code)
    inicio = response_code.find("[")
    fim = response_code.rfind("]")
    codigo_status = response_code[inicio + 1:fim]
    codigo_status = int(codigo_status)

    return codigo_status


if __name__ == '__main__':
    for site in sites:
        verificacao = urlscan(site)
        code_scan = get_code(verificacao)
        if code_scan == 200:
            print(f'\n{site}: Sucesso!\nCódigo HTTP 200\n')
        elif code_scan == 400:
            print(f'\n{site}: Erro!\nCódigo HTTP 400\n')
        else:
            print('Código não especificado')
