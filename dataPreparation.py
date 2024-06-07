import pandas as pd
import json
import numpy as np

def get_events_df(filepath='happenings.json'):

    f = open(filepath)
    happenings = json.load(f)
    f.close()
    happenings_converted = []
    for i in happenings:
        happenings_converted.append(i[0:2])

    df_happenings = pd.DataFrame(happenings_converted, columns=["Date", "Title"])

    df_happenings['Date'] = pd.to_datetime(df_happenings['Date'], dayfirst= True)

    week = []
    year = []
    for i in df_happenings['Date']:
        year.append(i.isocalendar()[0])
        week.append(i.isocalendar()[1])

    df_happenings["Year"] = year
    df_happenings["Week"] = week

    #print(df_happenings)
    return df_happenings

#print(get_events_df())


def prepare_data(filepath = "combined.csv"):
    data = pd.read_csv(filepath, na_values='-')
    data = data.fillna(0)

    data.rename(columns={"Value": "Deaths", "Value_Covid": "Covid_Deaths","Cases":"Covid_Cases"}, inplace=True)
    data["Normal_Deaths"] = data["Deaths"] - data["Covid_Deaths"]

    #data["Normal_Deaths_Total"] = data.groupby(["Year", "Week"])["Normal_Deaths"].cumsum()
    data["Deaths_Total"] = data.groupby(["Year", "Age"])["Deaths"].cumsum()
    data["Covid_Deaths_Total"] = data.groupby(["Year", "Age"])["Covid_Deaths"].cumsum()

    data["Normal_Deaths_Total"] = data["Deaths_Total"] - data["Covid_Deaths_Total"]

    data["Erstimpfung_All"] = data.groupby(["Age"])["Erstimpfung"].cumsum()
    data["Zweitimpfung_All"] = data.groupby(["Age"])["Zweitimpfung"].cumsum()
    data["Booster_All"] = data.groupby(["Age"])["Booster"].cumsum()


    #print(data)

    return data

#print(prepare_data("combined2.csv"))
