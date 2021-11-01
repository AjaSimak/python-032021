import requests
import pandas
import numpy
#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
#open("london_merged.csv", 'wb').write(r.content)

#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
#open("titanic.csv", 'wb').write(r.content)

df_titanic = pandas.read_csv("titanic.csv")

df_titanic_grouped = df_titanic.groupby(["Pclass", "Sex"])["Survived"].sum()
df_titanic_grouped = df_titanic_grouped.reset_index()

#print(df_titanic_grouped.head())

df_titanic_pivot_abs = pandas.pivot_table(df_titanic_grouped, index="Sex", columns="Pclass", values="Survived", aggfunc=numpy.sum, margins=True)
df_titanic_pivot_relativni = pandas.pivot_table(df_titanic, index="Sex", columns="Pclass", values="Survived", aggfunc=numpy.mean, margins=True)

print(df_titanic_pivot_abs)
print(df_titanic_pivot_relativni)

df_london = pandas.read_csv("london_merged.csv")

df_london = df_london.reset_index()
df_london["timestamp"] = pandas.to_datetime(df_london["timestamp"])
df_london["year"] = df_london["timestamp"].dt.year
df_london["month"] = df_london["timestamp"].dt.month
df_london["day"] = df_london["timestamp"].dt.day
df_london["hour"] = df_london["timestamp"].dt.hour

df_london_pivot = pandas.pivot_table(df_london, index=["month","day","hour"], columns="year", values="weather_code")
print(df_london_pivot)