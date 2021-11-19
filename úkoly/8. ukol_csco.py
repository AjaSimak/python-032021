import yfinance as yf
import pandas
import requests
import seaborn
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing


csco = yf.Ticker("CSCO")
csco_df = csco.history(period="5y")
#print(csco_df.head(30).to_string())

#zkouška klouzavých průměrů
#csco_df["SMA_12"] = csco_df["Close"].rolling(30, min_periods=1).mean()
#csco_df[["SMA_12", "Close"]].plot()
#csco_df["EMA"] = csco_df["Close"].ewm(alpha=0.01).mean()
#csco_df[["SMA_12", "EMA", "Close"]].plot()
#plt.show()

#Zobraz si graf autokorelace a podívej se, jak je hodnota ceny závislná na svých vlastních hodnotách v minulosti.
csco_df["Close"].autocorr(lag=30)

from statsmodels.graphics.tsaplots import plot_acf
plot_acf(csco_df["Close"])
plt.show()
#silná závislost vždy na předchozím dni

#Zkus použít AR model k predikci cen akcie na příštích 5 dní.
from statsmodels.tsa.ar_model import AutoReg

model = AutoReg(csco_df["Close"], lags=30, trend="ct", seasonal=False)
model_fit = model.fit()

predictions = model_fit.predict(start=csco_df.shape[0], end=csco_df.shape[0] + 5)
csco_df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
csco_df_with_prediction = pandas.concat([csco_df, csco_df_forecast])
csco_df_with_prediction[["Close", "Prediction"]].plot()
plt.show()

#Zobraz v grafu historické hodnoty (nikoli celou řadu,
# ale pro přehlednost např. hodnoty za posledních 50 dní) a tebou vypočítanou predikci.

model = AutoReg(csco_df["Close"], lags=30, trend="ct", seasonal=False)
model_fit = model.fit()

predictions = model_fit.predict(start=csco_df.shape[0], end=csco_df.shape[0] + 5)
csco_df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
csco_df_with_prediction = pandas.concat([csco_df, csco_df_forecast])
csco_df_with_prediction[["Close", "Prediction"]].tail(55).plot()
plt.show()

#kontrola posledních 50 dní
#print(csco_df.tail(50))
