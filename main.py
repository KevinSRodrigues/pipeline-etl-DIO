# Extract
# Importar e ler o arquivo .xlsx

# Transform
# Separar as avaliações em 3 níveis: Acima de 9.5 = Excelente / De 8.5 - 9.5 = Bom / Até 8.0 = Precisa melhorar
# Usar a API openai para montar frases personalizadas para cada funcionário

# Load
# Subir o repositório no GitHub

import pandas as pd
import requests
import json

# Pandas

sites = pd.read_csv('Lista_sites.csv')['Sites'].tolist()

# URLScan


def urlscan(site):
    headers = {'API-Key': 'c18387fb-4ace-44f4-b88a-dee47f067574',
               'Content-Type': 'application/json'}
    data = {"url": f"{site}", "visibility": "private"}
    response = requests.post(
        'https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
    return response, response.json()


if __name__ == '__main__':
    for site in sites:
        verificacao = urlscan(site)
        print(f'\n{site}:', f'\n{verificacao}\n')
