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

#print(lexikon_1.to_string())


def check_url(radek):
    if radek.image_src.startswith("https://zoopraha.cz/images/"):
        if isinstance(radek.image_src, str):
            if "jpg" in radek.image_src.lower():
                return
    else:
        print(radek.title)
for radek in lexikon_1.itertuples():
    check_url(radek)

