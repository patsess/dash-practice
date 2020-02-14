
import dash_core_components as dcc


def get_single_select_dropdown_child():
    # TODO: docstr
    child = dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'  # default value
    )
    return child


def get_multi_select_dropdown_child():
    # TODO: docstr
    child = dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],  # default values
        multi=True  # multi-select
    )
    return child
