from csv import reader
from pandas import DataFrame
from models.sale import Sale
from utils.formatters import price_formatter, ratting_formatter
def load_data():
    data = reader(open('datasets/amazon.csv'))
    headers = next(data)
    return DataFrame(data, columns=headers)

def process_data(data: DataFrame):
    sales = []
    for _, row in data.iterrows():
        sale = Sale()
        sale.product_name = row['product_name']
        sale.category = row['category']
        sale.actual_price = price_formatter(row['actual_price'])
        sale.rating = ratting_formatter(row['rating'])
        sales.append(sale)
    return sales
    
        
    