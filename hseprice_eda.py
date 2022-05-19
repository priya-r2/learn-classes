import pandas as pd

class Data:
    def __init__(self, df_path='./house_price.csv'):
        self.df_path = df_path
        # import IPython;
        # IPython.embed()
    def print_df_details(self):
        df = pd.read_csv(self.df_path)
        # import IPython;
        # IPython.embed()
        # df_saleprice = df.SalePrice
        # df_lotarea = df.LotArea
        return  df

data = Data()
data.print_df_details()