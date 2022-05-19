from hseprice_eda import Data
import matplotlib.pyplot as plt

class ScatterPlot:
    def __init__(self, sale_price, lot_area ):
        self.sale_price = sale_price
        self.lot_area = lot_area

    def display_scatter(self):
        plt.scatter(self.lot_area, self.sale_price)
        plt.title('Sale Price vs Lot Area')
        # Display Scatter plot
        plt.show()


data = Data()
df = data.print_df_details()
scatter_plot = ScatterPlot(df.SalePrice,df.LotArea)
scatter_plot.display_scatter()

