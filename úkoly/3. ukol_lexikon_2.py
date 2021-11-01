import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

lexikon_1 = pandas.read_csv("lexikon-zvirat.csv", sep=";")
print(lexikon_1.shape)
lexikon_1 = lexikon_1.dropna(how="all", axis="columns")
lexikon_1 = lexikon_1.dropna(how="all", axis="rows")
#print(lexikon_1.shape)

lexikon_1 = lexikon_1.set_index("id")
print(lexikon_1.info())

#print(lexikon_1.head().to_string())

#print(set(lexikon_1["id"]))


def popisek(radek):
    new_note = radek.str["title"] + radek.str["food"] + radek.str["food_note"] + radek.str["description"]
    return new_note

lexikon_1["new_note"] = lexikon_1.apply(popisek, axis=1)
print(lexikon_1)

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html