import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

stock = 'TSLA'
df = web.DataReader(stock, 'iex', start, end)
#df.reset_index(inplace=True)
#df.set_index('Date', inplace=True)
#df = df.drop('Symbol', axis=1)
#print(df.head())

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')
    ])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
    )
def update_graph(input_data):
    start = dt.datetime(2015, 1, 1)
    end = dt.datetime.now()
    df = web.DataReader(input_data, 'iex', start, end)
    #df.reset_index(inplace=True)
    #df.set_index('Date', inplace=True)
    #df = df.drop('Symbol', axis=1)

    return dcc.Graph(
        id='example-grah',
        figure={
            'data': [
                {'x': df.index, 'y': df['close'], 'type':'line', 'name': input_data}
                ],
            'layout': {
                'title': input_data
                }
            })

if __name__ == '__main__':
    app.run_server(debug=True)































































