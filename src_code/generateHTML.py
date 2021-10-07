# -*- coding: utf-8 -*-
# @Author: Nichsen   https://github.com/Nichsen 
# @Date:   2021-10-07 18:24:22
# @Last Modified by:   Nichsen   https://github.com/Nichsen 
# @Last Modified time: 2021-10-07 19:05:29
import datetime
import json
import os

import Data.HTML_GEN_DATA as HTML_DATA  # file containg variables with html stuff as strings

def genHtmlfile(): # "dump tool" generationg html form json data creating a simple html from "block code :-/"
    date= datetime.datetime.now()
    date = date.strftime("%Y_%m_%d")
    date2 = date
    path ="./Data/"
    calcFile = path + "calc_" + date +".json"

    x = []
    y1 = []
    y2 = []
    y3 = []

    with open(calcFile) as file:
        calcData= json.load(file)
        for rows in calcData:
            #rows["Active"] = rows["Confirmed"] - rows["Deaths"] - rows["Recovered"]
            date = str(rows["Date"])
            date = date[5:10]
            #x.insert(-1,date)
            x.append(date)
            y1.append(rows["Active"])
            y2.append(rows["Confirmed"])
            y3.append(rows["Deaths"])
            #print(rows["Date"])

    # Debug:
    #print(x)
    #print(y1)
    #print(y2)
    #print(y3)

    #generate HTML with json stuff:   
    htmlPath = "./HTML/report_"+ str(date2)+ ".html"
    f = open(htmlPath, "w")
    f.write(HTML_DATA.HEAD)
    f.write(str(x))
    f.write(HTML_DATA.MIDDLE1)
    f.write(str(y1))
    f.write(HTML_DATA.MIDDLE2)
    f.write(str(y2))
    f.write(HTML_DATA.MIDDLE3)
    f.write(str(y3))
    f.write(HTML_DATA.END)
    
    f.close()
    return htmlPath
