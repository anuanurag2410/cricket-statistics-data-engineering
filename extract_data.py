import requests
import csv

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

#querystring = {"formatType":"test"}

headers = {
	"X-RapidAPI-Key": "735d1841c7msh5908b4d65739c2ap1c43c0jsnff541268d977",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

params={
    'formatType':'odi'
}


response = requests.get(url, headers=headers, params=params)

if response.status_code==200:
    data=response.json().get('rank',[]) #Extracting Rank Data
    csv_filename='batsman_rankings.csv'

    if data:
        field_names=['rank','name','country'] #Specify required field names

        #Write data to CSV File with only specified field names
        with open(csv_filename,'w',newline='',encoding='utf-8') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=field_names)

            for entry in data:
                writer.writerow({field:entry.get(field) for field in field_names})

        print(f"Data Fetched Successfully and written to '{csv_filename}'")
    
    else:
        print("no data avaliable from the API.")
else:
    print("Failed to Fetch data:",response.status_code)