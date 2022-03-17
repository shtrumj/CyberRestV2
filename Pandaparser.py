import pandas as pd
import json


with open('CyberNet.json','r') as f:
        df = json.load(f)

#norm = pd.json_normalize(d, max_level=0)
norm  = pd.json_normalize(df, 'publication')
norm

#nycphil = pd.json_normalize(d)
#nycphil.head(3)



#df = pd.read_json('CyberNet.json')
#print(df.features)
#pd.DataFrame.from_records(bn).head()
#df = pd.json_normalize(df["publications"])
#df = pd.json_normalize(df["indicators"])
#print(df.head())
#df.head(self, n=5)