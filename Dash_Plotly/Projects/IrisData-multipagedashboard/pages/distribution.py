import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/distribution', name="Data Distribution")

####################### LOAD DATASET #############################

df = px.data.iris()

####################### HISTOGRAM ###############################
def create_distribution(col_name="species"):
    return px.histogram(data_frame=df, x=col_name, height=600, color="species")

####################### WIDGETS ################################
columns = ["species", "sepal_length", "sepal_width", "petal_length", "petal_length"]
dd = dcc.Dropdown(id="dist_column", options=columns, value="species", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.P("Select Column:"),
    dd,
    dcc.Graph(id="histogram")
])

####################### CALLBACKS ################################
@callback(Output("histogram", "figure"), [Input("dist_column", "value"), ])
def update_histogram(dist_column):
    return create_distribution(dist_column)

