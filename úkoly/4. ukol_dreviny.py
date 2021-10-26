import pandas
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt
from matplotlib import ticker



HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "andrea.stolfova"
USERNAME = f"andrea.stolfova@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "0g3AS.VgRA97tjnl"
engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)

dreviny = pandas.read_sql('dreviny', con=engine)
#print(dreviny.to_string())

dreviny_smrk = dreviny.dropna(subset=["dd_txt"])

smrk = dreviny_smrk[dreviny_smrk.dd_txt.str.contains("Smrk, jedle, douglaska")]

print(smrk.to_string())

dreviny_tezba = dreviny.dropna(subset=["druhtez_txt"])
nahodila_tezba = dreviny_tezba[dreviny_tezba.druhtez_txt.str.contains("Nahodilá těžba dřeva")]

print(nahodila_tezba.to_string())

#Vytvoř graf, který ukáže vývoj objemu těžby pro tabulku smrk. Pozor, řádky nemusí být seřazené podle roku.
smrk.sort_values(by="rok").plot(kind="bar", x="rok", y="hodnota", title="Vývoj objemu těžby smrk, jedle, douglaska v letech 2000-2020")
plt.show()

#ukáže vývoj objemu těžby v čase pro všechny typy nahodilé těžby
#První metoda: agreguj tabulku nahodila_tezba pomocí metody pivot_table a na výsledek zavolej metodu plot().
nahodila_tezba_pivot = pandas.pivot_table(nahodila_tezba, values="hodnota", index="rok", columns="prictez_txt")
print(nahodila_tezba_pivot.to_string())

ax = nahodila_tezba_pivot.plot(kind="barh", stacked=True, title="Typy nahodilé těžby v letech 2000-2020")
ax.set(xlabel="hodnota", ylabel="rok")
ax.legend(title="příčína")
ax.xaxis.set_major_formatter(ticker.EngFormatter())
plt.show()
