# Plotly Dash example
# For local deployment at localhost:8050
# The data series are displayed based on the checklist
#
# Created on 08/26/2023
# by Jin Zhu


from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go   #to install: pip3 install plotly
from plotly.subplots import make_subplots
import math

# Indicate the CSV File name, here we use an example dateset uploaded in github
filename = 'https://raw.githubusercontent.com/JZ2211/IIoT_module7/main/sensor15_log_2021_07_16.txt'

xdf = pd.read_csv(filename)
dataseries = list(xdf.columns)
datetime = dataseries[:2] #the first two columns are date and time

app = Dash(__name__)        #initialize the app

app.layout = html.Div([
    html.H1(children='Sensor Monitoring Dashboard', style={'textAlign':'center'}),
    html.Div(children=[
        html.Label('Select the data series:'),
        dcc.Checklist(
            id="checklist",
            options = dataseries[2:],
            value=[dataseries[2]]+dataseries[4:],
            inline=True,
            ),
        ]),
    dcc.Graph(id="graph-content"),
])

@callback(
    Output(component_id='graph-content', component_property='figure'),
    Input(component_id='checklist', component_property='value')
)
def update_plots(value):
    dt_series=datetime+value # a list of date, time, and checked colums
    df=xdf[dt_series]  #obtain the subset of original data frame based on checklist
    cols =df.columns  #the first two columns are 'Date' and ' Time', and rest are sensor data and we will plot each column as a subplot

    n_rows = df.shape[0]
    n_cols = df.shape[1]
    empty =" "
    rows = math.ceil(((n_cols-2)/2))

    #get the correct headers
    subplot_titles=[]
    for col in range(2,n_cols):
        subplot_titles.append(cols[col])

    #get the correct number of rows
    specs = []
    for row in range(rows):
        specs.append([{"type": "scatter"},{"type": "scatter"}])

    #make figure
    fig = make_subplots(
        rows=math.ceil(((n_cols-2)/2)), cols=2,
        shared_xaxes=True,
        vertical_spacing = 0.1,
        subplot_titles=subplot_titles,
        specs = specs)

    for col in range(2,n_cols):
        fig.add_trace(go.Scatter(x=df[cols[1]],y=df[cols[col]],mode="lines",name=cols[col]),row=math.floor(col/2), col=math.ceil(col%2)+1)
        fig.update_yaxes(title_text=cols[col], row=math.floor(col/2), col=math.ceil(col%2)+1)

    fig.update_xaxes(title_text = cols[1], row=rows)

    fig.update_layout(
        height=800,
        showlegend=False,
        title_text = "Sensor Monitoring Data from: Sensor 15" +" ||  Date: " + df[cols[0]][0] + " || Lastest update:" + df[cols[0]][n_rows-1] + "," + df[cols[1]][n_rows-1],
        )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
