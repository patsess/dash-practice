
import sys
from pathlib import Path
module_path = str(Path(__file__).absolute().parent)
if module_path not in sys.path:
    sys.path.append(module_path)  # e.g. '.../repos/<name_of_this_repo>'

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_auth
from dashpractice.layout.barchart import get_barchart_children
from dashpractice.layout.data_table import get_data_table_child
from dashpractice.layout.scatter_plot import get_scatter_plot_child
from dashpractice.layout.text import get_text_child, get_input_text_child
from dashpractice.layout.dropdown_menu import (
    get_single_select_dropdown_child, get_multi_select_dropdown_child)
from dashpractice.layout.check_buttons import (get_radio_button_child,
    get_checklist_child)

__author__ = 'psessford'

"""
tutorial - https://www.datacamp.com/community/tutorials/learn-build-dash-python
"""


COLOURS = {
    # 'background': '#111111',
    'background': 'white',
    'text': '#7FDBFF'
}


VALID_USERNAME_PASSWORD_PAIRS = [
    ['hello', 'world']
]


app = dash.Dash()
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
# app.config.suppress_callback_exceptions = True


def get_layout_children(page_name):
    # TODO: docstr
    children = [dcc.Dropdown(  # initialise
        id='index-menu',
        options=[
            {'label': 'Show all', 'value': 'all'},
            {'label': 'Show barplot', 'value': 'barplot'},
            {'label': 'Show scatter plot', 'value': 'scatter'}
        ],
        value=page_name  # default value
    )]

    if page_name == 'all':
        children += (
            get_barchart_children() +
            [get_data_table_child(), get_scatter_plot_child()] +
            [get_text_child()] +
            [html.Label('Dropdown'), get_single_select_dropdown_child()] +
            [html.Label('Multi-Select Dropdown'),
             get_multi_select_dropdown_child()] +
            [html.Label('Radio Items'), get_radio_button_child()] +
            [html.Label('Checkboxes'), get_checklist_child()] +
            [html.Label('Text Box'), get_input_text_child(),
             html.Div(id='output-of-text-input-div')]
        )
    elif page_name == 'barplot':
        children += get_barchart_children()
    elif page_name == 'scatter':
        children += [get_scatter_plot_child()]
    else:
        raise ValueError(f"unrecognised page_name {page_name}")

    return children


app.layout = html.Div(
    id='dashboard',
    style={'backgroundColor': COLOURS['background']},
    children=get_layout_children(page_name='all')
)


@app.callback(
    Output(component_id='dashboard', component_property='children'),
    [Input(component_id='index-menu', component_property='value')]
)
def get_layout_children_callback(page_name):
    # TODO: docstr
    return get_layout_children(page_name=page_name)


@app.callback(
    Output(component_id='output-of-text-input-div',
           component_property='children'),
    [Input(component_id='input-text', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
