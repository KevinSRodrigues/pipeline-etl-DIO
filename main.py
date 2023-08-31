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
