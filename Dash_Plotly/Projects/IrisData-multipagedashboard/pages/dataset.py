import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go
import plotly.express as px

dash.register_page(__name__, path='/dataset', name="Dataset")

####################### LOAD DATASET #############################
df = px.data.iris()

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    dash_table.DataTable(data=df.to_dict('records'),
                         page_size=20,
                         style_cell={"background-color": "lightgrey", "border": "solid 1px white", "color": "black", "font-size": "11px", "text-align": "left"},
                         style_header={"background-color": "#495053", "font-weight": "bold", "color": "white", "padding": "10px", "font-size": "18px"},
                        ),
])