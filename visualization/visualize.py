import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/processed_logistics.csv')

data['delivery_deviation'].hist()
plt.title("Delivery Deviation Distribution")
plt.show()
