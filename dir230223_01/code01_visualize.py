import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/train.csv')
df_small = df.query('store==1 & item == 1')
plt.ylabel("Sales")
plt.plot(df_small["date"], df_small["sales"], label="sales_daily")
plt.legend(loc='upper left')
plt.show()
