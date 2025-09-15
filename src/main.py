import matplotlib.pyplot as plt
from utils.data_helper import process_data, load_data


fig, ax = plt.subplots()
dataframe = load_data()
data = process_data(data=dataframe)

product_categories = list(set([sale.category for sale in data]))


sale_counts = [sum(1 for sale in data if sale.category == category) for category in product_categories]

bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

while len(bar_colors) < len(product_categories):
    bar_colors *= 2
bar_colors = bar_colors[:len(product_categories)]


ax.bar(product_categories, sale_counts, label=product_categories, color=bar_colors)
ax.set_xlabel('Categorias')
ax.set_ylabel('Total ventas')
ax.set_title('Total de ventas por categoria')
fig.figure.set_size_inches(20, 20)
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()
