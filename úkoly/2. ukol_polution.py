import requests
import pandas
import numpy
import seaborn as sns
import matplotlib.pyplot as plt

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
    open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

air_polution = pandas.read_csv("air_polution_ukol.csv")

air_polution["date"] = pandas.to_datetime(air_polution["date"])
air_polution["year"] = air_polution["date"].dt.year
air_polution["month"] = air_polution["date"].dt.month
air_polution_pivot = pandas.pivot_table(air_polution, index="year", columns="month", values="pm25", aggfunc=numpy.mean)

print(air_polution_pivot.to_string())


heat_map = sns.heatmap(air_polution_pivot, annot=True, linewidths=.3, cmap="PuBuGn")
plt.show()