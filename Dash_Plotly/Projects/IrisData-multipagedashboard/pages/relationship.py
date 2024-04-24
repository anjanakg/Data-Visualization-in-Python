import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/relationship', name="Data Relationship")

####################### DATASET #############################
df = px.data.iris()

####################### SCATTER CHART #############################
def create_scatter_chart(x_axis="sepal_width", y_axis="sepal_length"):
    return px.scatter(data_frame=df, x=x_axis, y=y_axis, color='species', height=600)

####################### WIDGETS #############################
columns = ["sepal_length", "sepal_width", "petal_length", "petal_length"]

x_axis = dcc.Dropdown(id="x_axis", options=columns, value="sepal_width", clearable=False)
y_axis = dcc.Dropdown(id="y_axis", options=columns, value="sepal_length", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    "X-Axis", x_axis, 
    "Y-Axis", y_axis,
    dcc.Graph(id="scatter")
])

####################### CALLBACKS ###############################
@callback(Output("scatter", "figure"), [Input("x_axis", "value"),Input("y_axis", "value"), ])
def update_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)

