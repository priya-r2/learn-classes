import pandas as pd
__all__ = ["ReadData",]

class ReadData:
    def __init__(self, df_path='./house_price.csv'):
        self.df_path = df_path
        # import IPython;
        # IPython.embed()
    def print_df_details(self):
        df = pd.read_csv(self.df_path)
        return  df