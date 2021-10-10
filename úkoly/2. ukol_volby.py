import requests
import pandas

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
    open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
    open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

prezidenti = pandas.read_csv("1976-2020-president.csv")
air_polution = pandas.read_csv("air_polution_ukol.csv")

prezidenti["Rank"] = prezidenti.groupby(["state"])["candidatevotes"].rank(ascending=False)
#print(prezidenti.head().to_string())

prezidenti_win = prezidenti.drop_duplicates(subset=["year", "state"], keep="first")
#print(prezidenti_win.to_string())

prezidenti_win = prezidenti_win.sort_values(["state", "year"])
prezidenti_win["party_simplified_next_year"] = prezidenti_win.groupby(["state"])["party_simplified"].shift(-1)
#print(prezidenti_win.head(30).to_string())

import numpy

prezidenti_win["win_porovnani"] = numpy.where(prezidenti_win["party_simplified"] == prezidenti_win["party_simplified_next_year"], "0", "1")
#print(prezidenti_win.head(30).to_string())


prezidenti_win["win_porovnani"] = prezidenti_win["win_porovnani"].astype(int)
prezidenti_win = prezidenti_win.groupby(["state"])["win_porovnani"].sum()
prezidenti_win = prezidenti_win.reset_index()
prezidenti_win = prezidenti_win.sort_values("win_porovnani", ascending=False)
print(prezidenti_win)