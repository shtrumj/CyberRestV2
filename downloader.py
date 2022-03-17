def downloadcyber():
    import requests
    url = 'https://cybernet.cyber.gov.il/api/rest/getIndicators?fromDate=2010-10-10_00%3A00%3A00'
    CNUSERNAME = 'soc_trot'
    XAPIKEY = '7384BBEFB00B40A2'
    response = requests.get(
        url, headers={'CN-USER-NAME': CNUSERNAME, 'X-API-KEY': XAPIKEY}
    )
    print(response.ok)
    with open('CyberNet.json', 'wb') as f:
        f.write(response.content)
