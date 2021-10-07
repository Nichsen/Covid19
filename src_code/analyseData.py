import json
import datetime
import os

def createCalcData(rawFile,calcFile):
    # calc raw data to use data
    with open(rawFile) as file:
        rawData= json.load(file)
    
    for rows in rawData:
        rows["Active"] = rows["Confirmed"] - rows["Deaths"] - rows["Recovered"]
        #print(rows["Active"])

    
    with open(calcFile, 'w') as outfile:
        json.dump(rawData, outfile)

    

def renderCurrentDay():
    date= datetime.datetime.now()
    date = date.strftime("%Y_%m_%d")
    path ="./Data/"

    if os.path.exists(path) == True:
        print(path, "existiert.")
        raw = path + "raw_" + date +".json"
        calc = path + "calc_" + date +".json"
        createCalcData(raw, calc)


