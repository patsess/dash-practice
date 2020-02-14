
import dash_table
from dashpractice.data import get_data


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
