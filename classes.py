#Libraries to Import
import requests
import csv
import json 
import dropbox
import pandas as pd

# Tokens
muvi_api_key = "MUVIKEY"
dropbox_api_token = "DROPBOXTOKEN"

# Query Parameter payload
payload = {
        "authToken": muvi_api_key, 
        "permalink": 'classes' , 
        "limit": '1000', 
        "lang_code": 'es',
        "orderby": 'lastupload'
        }

#Open the API and get the information 
data = requests.get(
            "https://cms.muvi.com/rest/getContentList", 
            params = payload
        ).json()

df = pd.DataFrame(data.get('movieList'))
df = df[['name', 'custom6']]

file_from = '/Users/michellezyman/Projects/Club247/contentlist.csv'
file_to = '/Club247/contentList.csv'

#drop
conn = dropbox.Dropbox(dropbox_api_token)

df_bytes = bytes(df.to_csv(index=False), 'utf8')

conn.files_upload(
    f=df_bytes,
    path=file_to,
    mode=dropbox.files.WriteMode.overwrite
)
