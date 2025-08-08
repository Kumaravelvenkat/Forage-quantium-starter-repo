from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('data/daily_sales_data_combined.csv')
df.sort_values('Date', inplace=True)
fig = px.line(df, x="Date", y="Sales")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel'),

    html.Div(children='''Sales Over Time'''),

    dcc.Graph(
        id='example-graph',
        figure= fig
    )
])

if __name__ =='__main__':
     app.run(debug=True)