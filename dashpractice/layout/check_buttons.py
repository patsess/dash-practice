
import dash_core_components as dcc


def get_radio_button_child():
    # TODO: docstr
    child = dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'  # default selected
    )
    return child


def get_checklist_child():
    # TODO: docstr
    child = dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']  # default selecteds
    )
    return child
