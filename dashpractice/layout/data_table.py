
import dash_table
from dashpractice.data import get_data

"""
help documentation - https://dash.plot.ly/datatable
"""


def get_data_table_child():
    # TODO: docstr
    df = get_data().head()
    df.reset_index(inplace=True)
    child = dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    )
    return child
