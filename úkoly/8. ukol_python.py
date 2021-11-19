import requests
import pandas
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/MLTollsStackOverflow.csv")
with open("MLTollsStackOverflow.csv", "wb") as f:
    f.write(r.content)

df = pandas.read_csv("MLTollsStackOverflow.csv")
print(df.tail(24).to_string())

#df = df.set_index("month")

#Vyber sloupec python.
#Proveď dekompozici této časové řady pomocí multiplikativního modelu. Dekompozici zobraz jako graf.
decompose = seasonal_decompose(df["python"], model='multiplicative', period=12)
decompose.plot()
plt.show()

#Vytvoř predikci hodnot časové řady pomocí Holt-Wintersovy metody na 12 měsíců.
#Sezónnost nastav jako 12 a uvažuj multiplikativní model pro trend i sezónnost.
#Výsledek zobraz jako graf.

from statsmodels.tsa.holtwinters import ExponentialSmoothing
mod = ExponentialSmoothing(df["python"], seasonal_periods=12, trend="multiplicative", seasonal="multiplicative")
res = mod.fit()
df["HWM"] = res.fittedvalues
df[["HWM", "python"]].plot()
df_forecast = pandas.DataFrame(res.forecast(12), columns=["Prediction"])
df_with_prediction = pandas.concat([df, df_forecast])
df_with_prediction[["python", "Prediction"]].plot()
plt.show()