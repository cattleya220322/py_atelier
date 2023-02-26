import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/train.csv', index_col=0, parse_dates=True)
df_small = df.query('store==1 & item == 1')
fig = plt.figure()
ax = fig.add_subplot()
ax.set_ylabel("Sales")
ax.plot(df_small["sales"], label="sales_daily")
ax.legend(loc='upper left')

plt.show()
