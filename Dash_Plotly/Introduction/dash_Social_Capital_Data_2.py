from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px
import pandas as pd                        # pip install pandas

# incorporate data into app
# Source - https://www.cdc.gov/nchs/pressroom/stats_of_the_states.htm
df = pd.read_csv("../Data/social_capital.csv")
print(df.head())

# Build components
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
mytitle = dcc.Markdown(children='')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=df.columns.values[2:],
                        value='Cesarean Delivery Rate',  # initial value displayed when page first loads
                        clearable=False)

# Customize own Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=8)
    ], justify='center'),
    dbc.Row([
        dbc.Col([mygraph], width=8),
        dbc.Col([dropdown], width=4)
    ]),
], fluid=True)

# Callback allows components to interact
@app.callback(
    Output(mygraph, 'figure'),
    Output(mytitle, 'children'),
    Input(dropdown, 'value')
)
def update_graph(column_name):  # function arguments come from the component property of the Input

    print(column_name)
    print(type(column_name))
    # https://plotly.com/python/bar-charts/
    # Modify the app so it plots a bar graph. 
    # The x-axis should represent states while the y-axis should represent the `column_name` from the dropdown. 
    fig = px.bar(data_frame=df, x='STATE', y=column_name)

    return fig, '# '+column_name  # returned objects are assigned to the component property of the Output


# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=8062)
