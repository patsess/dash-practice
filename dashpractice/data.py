
import pandas as pd


def get_data():
    # TODO: docstr
    df = pd.read_csv(
        'https://gist.githubusercontent.com/chriddyp/' +
        '5d1ea79569ed194d432e56108a04d188/raw/' +
        'a9f9e8076b837d541398e999dcbac2b2826a81f8/' +
        'gdp-life-exp-2007.csv', index_col=0)
    df.index.name = 'country_id'
    return df


if __name__ == '__main__':
    df = get_data()
    print(df.shape)
    print(df.iloc[0])
