
import dash_core_components as dcc


def get_text_child():
    # TODO: docstr
    markdown_text = '''
### Dash and Markdown
A lot of text
'''

    child = dcc.Markdown(children=markdown_text)
    return child


def get_input_text_child():
    # TODO: docstr
    child = dcc.Input(
        id='input-text',
        value='MTL',  # default/starting text
        type='text'
    )
    return child
