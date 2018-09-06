import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash tutorials'),
    dcc.Graph(id='example',
              figure={
                  'data': [
                      {'x':[1,2,3,4,5], 'y':[6,7,8,9,10], 'type':'line', 'name': 'boasts'},
                      {'x':[4,5,6,5,6], 'y':[10,9,8,7,6], 'type':'bar', 'name': 'cars'}
                      ],
                  'layout': {
                      'title': 'Basic Dash Example'
                      }
                  })
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
