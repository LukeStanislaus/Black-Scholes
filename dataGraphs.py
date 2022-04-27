import matplotlib.pyplot as plt
import csv
import datetime


c = open('HistoricalData_GameStop.csv','r')
fig, ax = plt.subplots()
o = csv.reader(c)
datesPrior = []
valuesPrior = []
datesSqueeze = []
valuesSqueeze = []
for r in o:
    if (r[0] == "Date"): continue
    date = datetime.datetime.strptime(r[0], "%m/%d/%Y")
    if (datetime.datetime(2017,1,1)<= date <= datetime.datetime(2020,5,1)):
        # r[1] is close price
        datesPrior.append(date)
        valuesPrior.append(float(r[1].replace("$", "")))
    elif(datetime.datetime(2021,1,1)<= date <= datetime.datetime(2021,3,1)):
        datesSqueeze.append(date)
        valuesSqueeze.append(float(r[1].replace("$", "")))
c.close()
plt.title("GameStop value between 2017 and mid 2020")
plt.plot(datesPrior,valuesPrior)
plt.xlabel("Date")
plt.ylabel("Price ($)")
# Make space for and rotate the x-axis tick labels
for label in ax.get_xticklabels():
        label.set_rotation(20)
        label.set_horizontalalignment('right')
plt.tight_layout()
plt.savefig("gameStopPriorValue.png")
plt.show()

fig, ax = plt.subplots()
plt.title("GameStop value during the squeeze of early 2021")
plt.plot(datesSqueeze,valuesSqueeze)
plt.xlabel("Date")
plt.ylabel("Price ($)")
# Make space for and rotate the x-axis tick labels
for label in ax.get_xticklabels():
        label.set_rotation(20)
        label.set_horizontalalignment('right')
plt.tight_layout()
plt.savefig("gameStopSqueezeValue.png")
plt.show()


c = open('VWAGY Historical Data.csv','r')
fig, ax = plt.subplots()
o = csv.reader(c)
dates = []
values = []
for r in o:
    if (r[0] == "ï»¿Date"): continue
    date = datetime.datetime.strptime(r[0], "%b %d, %Y")
    if (datetime.datetime(2008,9,1)<= date <= datetime.datetime(2009,1,1)):
        # r[1] is close price
        dates.append(date)
        values.append(float(r[1].replace("$", "")))
c.close()

plt.title("Volkswagen value between late 2008 and 2009")
plt.plot(dates,values)
plt.xlabel("Date")
plt.ylabel("Price ($)")
# Make space for and rotate the x-axis tick labels
for label in ax.get_xticklabels():
        label.set_rotation(20)
        label.set_horizontalalignment('right')
plt.tight_layout()
plt.savefig("volkswagenShortSqueeze.png")
plt.show()