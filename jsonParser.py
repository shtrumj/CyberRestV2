def parser():
    import json
    import pandas as pd
    import csv
    pd.set_option('max_colwidth', 100)

    with open('CyberNet.json') as f:
        d = json.load(f)
    raw = pd.json_normalize(d, record_path=['publications', 'indicators'])
    sha256 = raw[raw['type'].isin(['sha256'])]
    md5 = raw[raw['type'].isin(['md5'])]
    sha1 = raw[raw['type'].isin(['sha1'])]
    ip = raw[raw['type'].isin(['IP'])]
    domain = raw[raw['type'].isin(['domain'])]
    with open('output/sha256.csv', 'w') as myfile:
        wr = csv.writer(myfile)
        for word in sha256["value"]:
            wr.writerow([word])

    with open('output/md5.csv', 'w', ) as myfile:
        wr = csv.writer(myfile)
        for word in md5["value"]:
            wr.writerow([word])

    with open('output/sha1.csv', 'w', ) as myfile:
        wr = csv.writer(myfile)
        for word in sha1["value"]:
            wr.writerow([word])

    with open('output/ip_temp.csv', 'w', ) as myfile:
        wr = csv.writer(myfile)
        for word in ip["value"]:
            wr.writerow([word])

    with open('output/domains_temp.csv', 'w', ) as myfile:
        wr = csv.writer(myfile)
        for word in domain["value"]:
            wr.writerow([word])
