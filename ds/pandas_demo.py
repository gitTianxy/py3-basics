# encoding=utf-8
"""
I. data-structure
    1. Series
    2. DataFrame
"""
from pandas import Series, DataFrame


class SeriesDemo:
    """
    1. construction:
        * by array, dict;
        * specify index or not
    2. operations:
        * index
        * values
        * append
        * get element
        * filter element
        * bulk-calculations of elements
    """

    def __init__(self):
        data_list = ['ele_%s' % i for i in range(0, 5)]
        series_by_list = self.construct_by_list(data=data_list)
        print(series_by_list)
        index = ['idx_%s' % i for i in range(0, 5)]
        series_by_list_withidx = self.construct_by_list(data=data_list, index=index)
        print(series_by_list_withidx)
        print('---------------------')
        data_dict = {}
        for i in range(0, 5):
            data_dict['idx_%s' % i] = 'ele_%s' % i
        series_by_dict = self.construct_by_dict(data=data_dict)
        print(series_by_dict)
        specify_idx = ['idx_%s' % i for i in range(3, 8)]
        series_specify = self.construct_by_dict(data=data_dict, index=specify_idx)
        print(series_specify)
        series_append = series_by_dict.append(series_specify)
        print(series_append)
        series_not_null = series_append[series_append.notnull()]
        print(series_not_null)
        print('series_not_null[%s] = %s' % ('idx_1', self.get_by_index(series_not_null, 'idx_1')))

    def construct_by_list(self, **kwargs):
        data = kwargs.get('data')
        index = kwargs.get('index')
        return Series(data=data, index=index)

    def construct_by_dict(self, **kwargs):
        """
        当指定index时, data中有的填充进来,没有的用NanN
        :param kwargs:
        :return:
        """
        data = kwargs.get('data')
        index = kwargs.get('index')
        return Series(data=data, index=index)

    def get_values(self, series):
        return series.values

    def get_index(self, series):
        return series.index

    def get_by_index(self, series, idx):
        return series[idx]

    def calc_mutiply(self, series, weight):
        return series * weight

    def calc_sum(self, s1, s2):
        return s1 + s2


class DataFrameDemo:
    """
    construction:
        1. default
        2. specify column order
        3. specify row index
        2. construct by dict
    operations:
        1. get columns
        2. get column by name
        3. get item by col-name and row-idx
        4. add cols
        5. append rows
    TIPS:
        1. DataFrame 对象的每竖列都是一个 Series 对象
    """

    def __init__(self):
        disp_obj('--------------dateframe demo')
        data = {
            'name': ['zhang', 'wang', 'li'],
            'age': [1, 2, 3]
        }
        self.df = self.construct_col(data)
        disp_obj(self.df)
        cols = self.get_cols()
        disp_obj(cols)
        for col in cols:
            disp_obj(self.get_col(col))
        disp_obj(self.get_item('name', 1))

        self.df = self.construct_col(data, col_seqs=['age', 'name', 'except'])
        disp_obj(self.df, msg='df with specified colume-squence')

        self.df = self.construct_col(data, index=[10 * i for i in range(0, 3)])
        disp_obj(self.df, msg='df with self-defined idxs')

        data_dict = {
            'name': {
                '00': 'zhang',
                '01': 'wang',
                '02': 'li'
            },
            'age': {
                '00': 1,
                '01': 2,
                '02': 3
            }
        }
        self.df = self.construct_col(data_dict)
        disp_obj(self.df, msg='construct by dict')

        sex_col = Series(['male', 'female', 'male'], index=self.df['age'].index, name='sex')
        self.add_col(sex_col)
        disp_obj(self.df, msg='after add col')

        rows = [
            [4, 'wu', 'female'],
            [5, 'tian', 'male'],
        ]
        col_seqs = [col for col in self.df.columns]
        idxs = ['03', '04']
        self.add_row(rows, col_seqs, idxs)
        disp_obj(self.df, msg='after add rows')

    def construct_col(self, data, **kwargs):
        col_seqs = kwargs.get('col_seqs')
        idxs = kwargs.get('index')
        return DataFrame(data, columns=col_seqs, index=idxs)

    def get_cols(self):
        return self.df.columns

    def get_col(self, col_name):
        return self.df[col_name]

    def get_item(self, col_name, row_idx):
        return self.df[col_name][row_idx]

    def add_col(self, col):
        self.df[col.name] = col
        return self.df

    def add_row(self, rows, col_seq, idxs):
        """
        append is to generate a new df by concat two dfs
        :param rows:
        :param col_seq:
        :param idxs:
        :return:
        """
        df = DataFrame(rows, columns=col_seq, index=idxs)
        disp_obj(df)
        self.df = self.df.append(df)


def disp_obj(obj, **kwargs):
    msg = kwargs.get('msg')
    if msg is not None:
        print('\n***', msg)
    print(obj)


if __name__ == '__main__':
    SeriesDemo()
    DataFrameDemo()
