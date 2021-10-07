import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.dates as mdates
import json
import datetime
import os

date= datetime.datetime.now()
date = date.strftime("%Y_%m_%d")
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
        x.insert(0,date)
        y1.append(rows["Active"])
        y2.append(rows["Confirmed"])
        y3.append(rows["Deaths"])
        #print(rows["Date"])

# Debug:
#print(x)
#print(y1)
print(y2)
#print(y3)

#Plot:
#Gestaltung



#Daten anbinden
"""fig, ax =plt.subplots()
ax.plot(x, y1, label='test')
ax.plot(x, y2)
ax.plot(x, y3)

fig = plt.figure()
plt.show()"""

plt.plot(x, y1, label='actaul cases')
plt.plot(x, y2, label='infected')
plt.plot(x, y3, label='death')

plt.ylabel("Case numbers")
plt.xlabel("Date")
plt.axes


plt.title("COVID-19 Cases")
plt.legend()
plt.show()

