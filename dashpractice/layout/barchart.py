
import dash_core_components as dcc
import dash_html_components as html


COLOURS = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def get_barchart_children():
    # TODO: docstr
    children = [
        html.H1(
            children='Hello Dash',
            style={
                'textAlign': 'center',
                'color': COLOURS['text']
            }
        ),
        html.Div(children='Dash: A web application framework for Python.',
                 style={
                     'textAlign': 'center',
                     'color': COLOURS['text']
                 }),
        dcc.Graph(
            id='Graph1',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar',
                     'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar',
                     'name': u'Montréal'},
                ],
                'layout': {
                    'plot_bgcolor': COLOURS['background'],
                    'paper_bgcolor': COLOURS['background'],
                    'font': {
                        'color': COLOURS['text']
                    }
                }
            }
        )
    ]
    return children
