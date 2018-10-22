import dash
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

data_answers = [[9124, 8652, 7592, 7515], [8124, 8752, 7092, 7815], [0, 0, 1000, 0]]
labels = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'text': '#FFFFsFF'
}

#-----------------------------------
#диаграмма по всем ответам на все вопросы
app.layout = html.Div(children=[
    html.H1(children='Statistic', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div(children='''
        This are some statistics.
    ''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

        dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=np.arange(10),
                    y=np.random.sample(10),
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Date'},
                yaxis={'title': 'Activity'},
                margin={'l': 40, 'b': 40, 't': 30, 'r': 0},
                legend={'x': 0, 'y': 1},
                title= 'Activity of users',
            )
        }
    ),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4], 'y': data_answers[0], 'type': 'bar', 'name': 'The first possible answer'},
                {'x': [1, 2, 3, 4], 'y': data_answers[1], 'type': 'bar', 'name': 'The second possible answer'},
                {'x': [1, 2, 3, 4], 'y': data_answers[2], 'type': 'bar', 'name': 'The third possible answer'}
            ],
            'layout': {
                'title': 'Answers for questions'
            }
        }
    ),
        dcc.Graph(
        id='graph1',
        figure={
            'data': [
                {'x': [1, 2, 3, 4], 'y': [data_answers[0][0], data_answers[1][0], data_answers[2][0]], 'type': 'bar'}
            ],
            'layout': {
                'title': 'Answers for the first question'
            }
        }
    ),
        dcc.Graph(
        id='graph2',
        figure={
            'data': [
                {'x': [1, 2, 3, 4], 'y': [data_answers[0][1], data_answers[1][1], data_answers[2][1]], 'type': 'bar'}
            ],
            'layout': {
                'title': 'Answers for the second question'
            }
        }
    ),
        dcc.Graph(
        id='graph3',
        figure={
            'data': [
                {'x': [1, 2, 3, 4], 'y': [data_answers[0][2], data_answers[1][2], data_answers[2][2]], 'type': 'bar'}
            ],
            'layout': {
                'title': 'Answers for the third question'
            }
        }
    ),
        dcc.Graph(
        id='graph4',
        figure={
            'data': [
                {'x': [1, 2, 3, 4], 'y': [data_answers[0][3], data_answers[1][3], data_answers[2][3]], 'type': 'bar'}
            ],
            'layout': {
                'title': 'Answers for the fourth question'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)