import requests

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
    open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

import pandas

castice = pandas.read_csv("air_polution_ukol.csv")

castice["date"] = pandas.to_datetime(castice["date"])
castice["year"] = castice["date"].dt.year
castice["month"] = castice["date"].dt.month

#print(castice.head())

from scipy.stats import mannwhitneyu
# Z dat vyber data za leden roku 2019 a 2020.
data_2019 = castice[(castice["year"] == 2019) & (castice["month"] == 1)]
data_2020 = castice[(castice["year"] == 2020) & (castice["month"] == 1)]

#x = castice[(castice["year"] == 2019) & (castice["month"] == 1)]["pm25"]
#y = castice[(castice["year"] == 2020) & (castice["month"] == 1)]["pm25"]
x = data_2019["pm25"]
y = data_2020["pm25"]

castice_gb = castice.groupby(["year", "month"])["pm25"].mean()
print(castice_gb.to_string())

print(mannwhitneyu(x, y))

#H0: Průměrné množství jemných částic ve vzduch pro sledované roky 2019 a 2020 pro měsíc leden je stejné.
#H1: Průměrné množství jemných částic ve vzduch pro sledované roky 2019 a 2020 pro měsíc leden je rozdílné.
# Na hladině významnosti 5 % je p-hodnota 1,1 %, tzn. nulová hypotzka je zamítnuta, průměrné množství jemných částic ve
# vzduchu pro sledované období v měsíci lednu roku 2019 a 2020 se liší (v roce 2020 bylo vyšší než v roce 2019).

