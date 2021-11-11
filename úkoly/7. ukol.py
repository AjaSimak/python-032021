import requests
import pandas
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
    f.write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
with open("Concrete_Data_Yeh.csv", "wb") as f:
    f.write(r.content)

ryby = pandas.read_csv("Fish.csv")
cement = pandas.read_csv("Concrete_Data_Yeh.csv")

#print(ryby.head())
#print(cement.head().to_string())



mod = smf.ols(formula="csMPa ~ age + cement + slag + flyash + water + superplasticizer + coarseaggregate + fineaggregate", data=cement)
res = mod.fit()
print(res.summary())

#koeficient determinace činí 0.616, což není vysoké číslo, tzn. predikce kompresní síly betonu na základě jednotlivých složek betonu a stáří
# není spolehlivá, ke zpřesnění modelu je možné zjistit, které proměnné jsou korelované, v případě vysoké korelace jednu z proměnných odstranit
# dále zjistit, jestli v DF nechybí hodnoty

#kontrola prázdných hodnot - hodnoty nechybí
cement.isna().sum()

#kontrola korelace mezi proměnnými - není výzmnamná korelace mezi proměnnými
seaborn.heatmap(cement.corr(), annot=True, linewidths=.5, fmt=".2f", cmap="Blues", vmax=1)
plt.show()

# negativní ovlivnění síly betonu z uvedených složek je voda -> s rostoucím množstvím vody klesá kompresní síla betonu


mod = smf.ols(formula="Weight ~ Length2", data=ryby)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula="Weight ~ Length2 + Height", data=ryby)
res = mod.fit()
print(res.summary())
#pokud přidáme váhu, koeficient determinace se zpřesní z 0,844 na 0,875, tj. predikce se zpřesní

prumer_ryby = ryby.groupby("Species")["Weight"].mean()
print(prumer_ryby)
ryby["druh_prumer_ryby"] = ryby["Species"].map(prumer_ryby)
predictors = ["Length2", "Height", "druh_prumer_ryby"]

mod = smf.ols(formula="Weight ~ Length2 + Height + druh_prumer_ryby", data=ryby)
res = mod.fit()
print(res.summary())

#po přidání druh_prumer_ryby je koeficient determinace 0,9 - model je opět o trochu více zpřesněn

#pokusy
from scipy.stats import norm
seaborn.distplot(ryby["Weight"], fit=norm).set_title("Váhové rozložení")
#plt.show()

from scipy.stats import lognorm
seaborn.distplot(ryby["Weight"], fit=lognorm).set_title("Váhové rozložení")
#plt.show()

import numpy
from scipy.stats import norm
seaborn.distplot(numpy.log(ryby["Weight"]), fit=norm).set_title("Váhové rozložení")
#plt.show()