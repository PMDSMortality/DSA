import pandas as pd
import plotly
import plotly.graph_objs as go
import dataPreparation as dp


def get_death_cases_graph(data, year, startweek=1, endweek=52, age="gesamt", lookback=5):
    data_filtered = data.query("Year == @year and Week >= @startweek and Week <= @endweek and Age == @age")
    lookback_data = data.query(
        "Year < @year and Year >= @year-@lookback and Week >= @startweek and Week <= @endweek and Age == @age")

    expected_deaths = lookback_data.groupby(["Week"]).agg({"Deaths_Total": ["mean", "std"]}).reset_index()
    expected_deaths["Deaths_Total_Low"] = expected_deaths.Deaths_Total["mean"] - expected_deaths.Deaths_Total["std"]
    expected_deaths["Deaths_Total_High"] = expected_deaths.Deaths_Total["mean"] + expected_deaths.Deaths_Total["std"]

    # print(data_filtered)
    # print(lookback_data)
    # print(expected_deaths)

    fig = go.Figure()

    # ToDo Farben für die Graphen festlegen

    # Fälle pro Woche
    fig.add_trace(
        go.Scatter(x=data_filtered["Week"], y=data_filtered["Normal_Deaths"], name="Normale Sterbefälle pro Woche",
                   line=dict(color='blue', width=5, dash='solid'), legendrank=5))
    fig.add_trace(
        go.Scatter(x=data_filtered["Week"], y=data_filtered["Covid_Deaths"], name="Covid Sterbefälle pro Woche",
                   line=dict(color='orange', width=5, dash='solid'), legendrank=4))

    # Fälle nach Woche

    fig.add_trace(
        go.Bar(x=data_filtered["Week"], y=data_filtered["Normal_Deaths_Total"], name="Normale Sterbefälle nach Woche x",
               marker=dict(color='blue', opacity=0.5), legendrank=3))
    fig.add_trace(
        go.Bar(x=data_filtered["Week"], y=data_filtered["Covid_Deaths_Total"], name="Covid Sterbefälle nach Woche x",
               marker=dict(color='orange', opacity=0.5), legendrank=2))
    fig.update_layout(barmode='stack')

    # Prognose der erwarteten Sterbefälle

    # Prognose
    fig.add_trace(
        go.Scatter(x=data_filtered["Week"], y=expected_deaths.Deaths_Total["mean"], name="Erwartete Sterbefälle",
                   line=dict(color='red', dash='solid'), legendgroup=1, legendrank=1))

    # Varianzbereich der Prognose
    fig.add_trace(go.Scatter(
        x=data_filtered["Week"].tolist() + data_filtered["Week"].tolist()[::-1],
        y=expected_deaths["Deaths_Total_High"].tolist() + expected_deaths["Deaths_Total_Low"].tolist()[::-1],
        fill='toself',
        fillcolor='red',
        line_color='red',
        opacity=0.2,
        legendgroup=1,
        showlegend=False
    ))

    fig.update_layout(title=f"Sterbefälle in {year} von Woche {startweek} bis {endweek}({age})",
                      title_x=0.5,
                      xaxis_title="Woche",
                      yaxis_title="Sterbefälle")

    return fig
    # fig.show()


# data = dp.prepare_data()
# print(data.query("Age == '0-34'")[["Normal_Deaths", "Normal_Deaths_Total"]])
# print(data.loc[:,["Deaths","Covid_Deaths","Normal_Deaths"]])
# fig = get_death_cases_graph(data, year=2021, startweek=1, endweek=52, age="gesamt", lookback = 3)
# fig.show()


def get_covid_line_graph(data, value_to_plot="Covid_Cases", year=2020, startweek=1, endweek=52, age="gesamt"):
    data_filtered = data.query("Year == @year and Week >= @startweek and Week <= @endweek and Age == @age").loc[:,
                    ["Week", value_to_plot]]


    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data_filtered["Week"],
        y=data_filtered[value_to_plot],
    ))

    fig.update_layout(title=f"{value_to_plot} in {year} von Woche {startweek} bis {endweek}({age})",
                      title_x=0.5,
                      xaxis_title="Woche",
                      yaxis_title=value_to_plot)

    #fig.show()
    #print(data_filtered)

    return fig


#data = dp.prepare_data()
#print(data)
#get_covid_line_graph(data, value_to_plot="Inzidenz")