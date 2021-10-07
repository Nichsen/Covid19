import requests
import datetime
import json
#  =========== FUNCTIONS =====
def storeData(data):
    date= datetime.datetime.now()
    date = date.strftime("%Y_%m_%d")
    path= "./Data/raw_" + date + ".json"
    #print(path)
    jData= json.loads(data)
    """file = open(path,"w")
    file.write(str(jData))
    file.close()"""
    with open(path, 'w') as outfile:
        json.dump(jData, outfile)

# ===============================================================================================================================================
def apiCall():
    #response = requests.get("https://api.covid19api.com/summary")
    link = "https://api.covid19api.com/country/germany/status/confirmed/live?from=2020-03-01T00:00:00Z&to=2020-04-24T00:00:00Z"
    link = "https://api.covid19api.com/country/germany"
    response = requests.get(link)
    # Print the status code of the response.
    if response.status_code == 200:
        print("Erfolg API abfrage: " + str(response.status_code))
        data = response.content
        storeData(data)
    else:
        print("PROBLEME MIT DER API! " + str(response.status_code))

    #print(response.content)


