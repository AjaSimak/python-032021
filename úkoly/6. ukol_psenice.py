import requests

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
    open("psenice.csv", 'w', encoding="utf-8").write(r.text)

import pandas

psenice = pandas.read_csv("psenice.csv")

print(psenice.head())

from scipy.stats import mannwhitneyu

x = psenice["Rosa"]
y = psenice["Canadian"]
print(mannwhitneyu(x, y))

#H0: Délky odrůd pšenice Rosa a Canadian jsou stejné.
#H1: Délky odrůd pšenice Rosa a Canadian jsou odlišné.
#Pro hladinu významnosti 5 % je p-hodnota velmi nízká, nulovou hypotézu zamínáme, délky odrůd pšenice jsou odlišné.