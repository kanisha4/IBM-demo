# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:06:45 2021

@author: Kanisha
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go   #for scatter graph
import pandas as pd

data = pd.read_csv("dth_data_1.csv")

ott_subs = dict(data.ott_subscription.value_counts())
#print(data.ott_subscription.value_counts())

fig = px.bar(x=list(ott_subs.keys()), y=list(ott_subs.values()), title="Popularity of OTT Platform ")

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id = "bar-graph", figure = fig)
    ])

if __name__ == '__main__':
    app.run_server(debug=False)
