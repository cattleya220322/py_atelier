# ２０１３年に絞ってデータを確認
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/train.csv', index_col=0, parse_dates=True)
df_small = df.query('store==1 & item == 1')
df_small = df_small[df_small.index.year == 2013]

df_small['rolling_mean_3'] = df_small['sales'].rolling(window=3).mean()

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel("date")
ax.set_ylabel('daily_Sales')
ax.plot(df_small['sales'], color='red', label='row_data')
ax.plot(df_small['rolling_mean_3'], color='blue', label='rolling_mean')
ax.legend(loc='upper right')

plt.show()
