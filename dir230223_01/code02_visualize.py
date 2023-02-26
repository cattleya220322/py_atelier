# ２０１３年に絞ってデータを確認
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/train.csv', index_col=0, parse_dates=True)
df_small = df.query('store==1 & item == 1')
df_small_01 = df_small[df_small.index.year == 2013]

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel("date")
ax.set_ylabel('daily_Sales')
ax.plot(df_small_01['sales'], color='red', label='2013')
ax.legend(loc='upper right')

plt.show()
