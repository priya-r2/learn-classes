from house_price_eda import ReadData
from scatter_plot import ScatterPlot

data_path = './house_price.csv'
eda_obj = ReadData(data_path)
df = eda_obj.print_df_details()
data_viz = ScatterPlot(df.SalePrice, df.LotArea)
data_viz.display_scatter()