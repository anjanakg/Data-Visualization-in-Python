import dash
from dash import html

dash.register_page(__name__, path='/', name="Introduction")

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("Dataset Information"),
        "What do the instances in this dataset represent: Each instance is a plant",
        html.Br(),html.Br(),
        "This is one of the earliest datasets used in the literature on classification methods and widely used in statistics and machine learning.  The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant.  One class is linearly separable from the other 2; the latter are not linearly separable from each other.",
        html.Br(), html.Br(),
        "Predicted attribute: class of iris plant.",
    ]),
    html.Div(children=[
        html.Br(),
        html.H2("Data Variables"),
        html.B("species: "), "virginica, versicolor, setosa",
        html.Br(),
        html.B("sepal_length"),
        html.Br(),
        html.B("sepal_width"),
        html.Br(),
        html.B("petal_length"), 
        html.Br(),
        html.B("petal_length"),
    ])
], className="bg-light p-4 m-2")