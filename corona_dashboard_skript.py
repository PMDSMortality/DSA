import dataPreparation as dp
import graphs

data,policies = dp.prepare_data()

# print(data)

# Import packages
import numpy
from dash import Dash, html, dash_table, Input, Output, State, callback, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly
# import dash_core_components as dcc
# import dash_html_components as html

import plotly.express as px
import plotly.graph_objs as go

# import dash_table
# import pandas as pd


# Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
# app.layout = html.Div(children='My First App with Data')


app.layout = (

    html.H1('Corona Dashboard', style={'textAlign': 'center'}),
    dbc.Row([
        dbc.Col([
            html.Div([
                "Jahr",
                dcc.Input(
                    id="input_year",
                    type="number",
                    min=2020,
                    max=2023,
                    step=1,
                    value=2020

                )
            ])
        ], width='auto'),

        dbc.Col([
            html.Div([
                "Wochen",
                dcc.RangeSlider(min=1, max=52, step=1, value=[1, 52], id="week-slider")
            ])
        ]),

        dbc.Col([
            html.Div([
                "Lookback",
                dcc.Input(
                    id="input_lookback",
                    type="number",
                    min=3,
                    max=5,
                    step=1,
                    value=3
                )
            ])
        ], width='auto')
    ]),

    html.Div([
        "Maßnahmen-Score",
        dcc.RadioItems(
            id="radio-item_policy_score",
            options=[
                {'label':'Government Response Index', 'value':'Government Response Index'},
                {'label': 'Containment Health Index', 'value': 'Containment Health Index'},
                {'label': 'Stringency Index', 'value': 'Stringency Index'},
                {'label': 'Economic Support Index', 'value': 'Economic Support Index'},
                {'label': 'Population Vaccinated', 'value': 'Population Vaccinated'},
            ],
            value='Government Response Index',
            inline=True,
            inputStyle={'marginLeft': '20px', 'marginRight': '5px'},
        ),

    ]),



    html.Div(id="graph-grid", children=[
        dbc.Row([

            # Spalte mit aktiven Corona-Fällen

            # Spalte mit Coronafällen

            dbc.Col([
                dcc.Graph(id='covid_cases_all', figure=graphs.get_covid_line_graph(data=data, policies= policies, year=2020)),
                dcc.Graph(id='covid_cases_0-34', figure=graphs.get_covid_line_graph(data=data, policies= policies,year=2020, age="0-34")),
                dcc.Graph(id='covid_cases_35-59',
                          figure=graphs.get_covid_line_graph(data=data, policies= policies,year=2020, age="35-59")),
                dcc.Graph(id='covid_cases_60-79',
                          figure=graphs.get_covid_line_graph(data=data, policies= policies,year=2020, age="60-79")),
                dcc.Graph(id='covid_cases_80+', figure=graphs.get_covid_line_graph(data=data,policies= policies, year=2020, age="80+"))
            ]),

            # Spalte mit Hospitalisierungfällen
            dbc.Col([
                dcc.Graph(id='option_graph_all',
                          figure=graphs.get_covid_line_graph(data=data,policies= policies, year=2020, value_to_plot="Hospi_Cases")),
                dcc.Graph(id='option_graph_0-34',
                          figure=graphs.get_covid_line_graph(data=data, policies= policies,year=2020, age="0-34",
                                                             value_to_plot="Hospi_Cases")),
                dcc.Graph(id='option_graph_35-59',
                          figure=graphs.get_covid_line_graph(data=data, policies= policies,year=2020, age="35-59",
                                                             value_to_plot="Hospi_Cases")),
                dcc.Graph(id='option_graph_60-79',
                          figure=graphs.get_covid_line_graph(data=data, policies= policies, year=2020, age="60-79",
                                                             value_to_plot="Hospi_Cases")),
                dcc.Graph(id='option_graph_80+',
                          figure=graphs.get_covid_line_graph(data=data, policies= policies, year=2020, age="80+",
                                                             value_to_plot="Hospi_Cases"))
            ]),

            # Spalte mit Todesfällen
            dbc.Col([
                dcc.Graph(id='death_all', figure=graphs.get_death_cases_graph(data=data,policies=policies, year=2020)),
                dcc.Graph(id='death_0-34', figure=graphs.get_death_cases_graph(data=data,policies=policies, year=2020, age="0-34")),
                dcc.Graph(id='death_35-59', figure=graphs.get_death_cases_graph(data=data,policies=policies, year=2020, age="35-59")),
                dcc.Graph(id='death_60-79', figure=graphs.get_death_cases_graph(data=data, policies=policies,year=2020, age="60-79")),
                dcc.Graph(id='death_80+', figure=graphs.get_death_cases_graph(data=data,policies=policies, year=2020, age="80+"))
            ], width=6)
        ])

    ])

)


@callback(
    Output('covid_cases_all', 'figure'),
    Output('covid_cases_0-34', 'figure'),
    Output('covid_cases_35-59', 'figure'),
    Output('covid_cases_60-79', 'figure'),
    Output('covid_cases_80+', 'figure'),
    Input('input_year', 'value'),
    Input('week-slider', 'value'),
    Input('radio-item_policy_score', 'value'),
)
def update_graph_covid_cases(year, weekintervall, policy_type):
    startweek = weekintervall[0]
    endweek = weekintervall[1]
    fig_cca = graphs.get_covid_line_graph(data=data, policies= policies, year=year, startweek=startweek, endweek=endweek, policy_type=policy_type)
    fig_cc_034 = graphs.get_covid_line_graph(data=data, policies= policies,year=year, age="0-34", startweek=startweek, endweek=endweek, policy_type=policy_type)
    fig_cc_3559 = graphs.get_covid_line_graph(data=data, policies= policies,year=year, age="35-59", startweek=startweek, endweek=endweek, policy_type=policy_type)
    fig_cca_6079 = graphs.get_covid_line_graph(data=data,policies= policies, year=year, age="60-79", startweek=startweek, endweek=endweek, policy_type=policy_type)
    fig_cca_80p = graphs.get_covid_line_graph(data=data, policies= policies,year=year, age="80+", startweek=startweek, endweek=endweek, policy_type=policy_type)

    return fig_cca, fig_cc_034, fig_cc_3559, fig_cca_6079, fig_cca_80p


@callback(
    Output("option_graph_all", "figure"),
    Output("option_graph_0-34", "figure"),
    Output("option_graph_35-59", "figure"),
    Output("option_graph_60-79", "figure"),
    Output("option_graph_80+", "figure"),
    Input('input_year', 'value'),
    Input('week-slider', 'value'),
    Input('radio-item_policy_score', 'value'),
)
# Input für Radio Button der bestimmt welcher Wert gezeigt wird
def update_graph_opt(year, weekintervall, policy_type):
    startweek = weekintervall[0]
    endweek = weekintervall[1]
    fig_opt_all = graphs.get_covid_line_graph(data=data,policies= policies, year=year, startweek=startweek, endweek=endweek,
                                              value_to_plot="Hospi_Cases", policy_type=policy_type)
    fig_opt_034 = graphs.get_covid_line_graph(data=data, policies= policies,year=year, age="0-34", startweek=startweek, endweek=endweek,
                                              value_to_plot="Hospi_Cases", policy_type=policy_type)
    fig_opt_3559 = graphs.get_covid_line_graph(data=data, policies= policies,year=year, age="35-59", startweek=startweek, endweek=endweek,
                                               value_to_plot="Hospi_Cases", policy_type=policy_type)
    fig_opt_6079 = graphs.get_covid_line_graph(data=data,policies= policies, year=year, age="60-79", startweek=startweek, endweek=endweek,
                                               value_to_plot="Hospi_Cases", policy_type=policy_type)
    fig_opt_80p = graphs.get_covid_line_graph(data=data,policies= policies, year=year, age="80+", startweek=startweek, endweek=endweek,
                                              value_to_plot="Hospi_Cases", policy_type=policy_type)
    return fig_opt_all, fig_opt_034, fig_opt_3559, fig_opt_6079, fig_opt_80p


@callback(
    Output("death_all", "figure"),
    Output("death_0-34", "figure"),
    Output("death_35-59", "figure"),
    Output("death_60-79", "figure"),
    Output("death_80+", "figure"),
    Input("input_year", 'value'),
    Input("week-slider", "value"),
    Input("input_lookback", "value"),
    Input('radio-item_policy_score', 'value'),
)
def update_graph_death(year, weekintervall, lookback, policy_type):
    startweek = weekintervall[0]
    endweek = weekintervall[1]

    fig_death_all = graphs.get_death_cases_graph(data=data, policies=policies,year=year, startweek=startweek, endweek=endweek,
                                                 lookback=lookback,policy_type = policy_type)
    fig_death_034 = graphs.get_death_cases_graph(data=data,policies=policies, year=year, startweek=startweek, endweek=endweek,
                                                 lookback=lookback,
                                                 age="0-34",policy_type = policy_type)
    fig_death_3559 = graphs.get_death_cases_graph(data=data, policies=policies,year=year, startweek=startweek, endweek=endweek,
                                                  lookback=lookback,
                                                  age="35-59",policy_type = policy_type)
    fig_death_6079 = graphs.get_death_cases_graph(data=data,policies=policies, year=year, startweek=startweek, endweek=endweek,
                                                  lookback=lookback,
                                                  age="60-79",policy_type = policy_type)
    fig_death_80p = graphs.get_death_cases_graph(data=data, policies=policies,year=year, startweek=startweek, endweek=endweek,
                                                 lookback=lookback,
                                                 age="80+",policy_type = policy_type)

    return fig_death_all, fig_death_034, fig_death_3559, fig_death_6079, fig_death_80p


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
