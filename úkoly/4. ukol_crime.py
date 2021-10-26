import pandas
from sqlalchemy import create_engine, inspect
import numpy

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "andrea.stolfova"
USERNAME = f"andrea.stolfova@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "0g3AS.VgRA97tjnl"
engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)

crime = pandas.read_sql('crime', con=engine)

#print(crime.head().to_string())

#Pomocí SQL dotazu si připrav tabulku o krádeži motorových vozidel (sloupec PRIMARY_DESCRIPTION by měl mít hodnotu "MOTOR VEHICLE THEFT").

motor_vozidla = crime[crime.PRIMARY_DESCRIPTION.str.contains("MOTOR VEHICLE THEFT")]
#print(motor_vozidla.to_string())

#jen informace o krádeži aut (hodnota "AUTOMOBILE" ve sloupci SECONDARY_DESCRIPTION).
motor_vozidla_auto = motor_vozidla[motor_vozidla.SECONDARY_DESCRIPTION.str.contains("AUTOMOBILE")]
#print(motor_vozidla_auto.to_string())

#Ve kterém měsíci dochází nejčastěji ke krádeži auta?
motor_vozidla_auto["DATE_OF_OCCURRENCE"] = pandas.to_datetime(motor_vozidla_auto["DATE_OF_OCCURRENCE"])
motor_vozidla_auto["year"] = motor_vozidla_auto["DATE_OF_OCCURRENCE"].dt.year
motor_vozidla_auto["month"] = motor_vozidla_auto["DATE_OF_OCCURRENCE"].dt.month
#print(motor_vozidla_auto.head().to_string())

#motor_vozidla_auto["rows"]=numpy.arange(len(motor_vozidla_auto))
motor_vozidla_auto["rows"] = motor_vozidla_auto.groupby(["year", "month"]).cumcount()
motor_vozidla_auto = motor_vozidla_auto.groupby(["year", "month"])["rows"].sum().sort_values(ascending=False)
print(motor_vozidla_auto)

#motor_vozidla_auto_pivot = pandas.pivot_table(motor_vozidla_auto, index="year", columns="month", values=numpy.arange(len(motor_vozidla_auto), aggfunc=numpy.sum)
#print(motor_vozidla_auto_pivot)
#jak by to bylo přes pivotku?