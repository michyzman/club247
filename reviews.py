#Libraries Imported 
import requests #Read API
import json #Decode JSON FIle
import csv #create a .csv file 

#API KEY from MUVI 
api_key = "MUVIKEY"
#read getContentList API
contentListAPI = requests.get("https://cms.muvi.com/rest/getContentList?authToken=MUVIKEY&permalink=classes&limit=100").json()
#open a new .csv file 
outputWriter = csv.writer(open("test.csv", "w"), lineterminator = '\n')
for item in contentListAPI ['movieList']:
    #parameter for Reviews API
    payload = {"authToken": api_key, "permalink": 'movieList', "offset": '0', "limit": '1000', "content_id": item ['movie_id'] }
    #read reviews API
    reviewsAPi = requests.get("https://cms.muvi.com/rest/Reviews", params = payload).json()
    #read only the videos that have reviews 
    if  reviewsAPi ['item_count'] == 0:
        continue
    for item2 in  reviewsAPi ['review']:
        #print the content in the .csv file 
        outputWriter.writerow([item['movie_id'], item ['custom6'],item2['rating'], item2['content'], item2['user_name'], item2['date']])
    
