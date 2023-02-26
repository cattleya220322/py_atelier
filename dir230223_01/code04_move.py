# ２０１３年に絞ってデータを確認
from sklearn.metrics import mean_absolute_error
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/train.csv', index_col=0, parse_dates=True)
df_small = df.query('store==1 & item == 1')
df_small = df_small[df_small.index.year == 2013]

df_small_14 = df.query('store==1 & item == 1')
df_small_14 = df_small_14[df_small_14.index.year == 2014]

# 日付列の追加（2013 と 2014 のデータを重ねる為）
days = [i for i in range(1, 366)]
df_small["days"] = days
df_small_14["days"] = days

# 移動平均を計算・列に追加
df_small['rolling_mean_3'] = df_small['sales'].rolling(window=3).mean()

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel("date")
ax.set_ylabel('daily_Sales')
plt.plot(df_small_14['days'], df_small_14["sales"],
         color="red", label='2014_raw')
ax.plot(df_small['days'], df_small['rolling_mean_3'],
        color='blue', label='2013_rolling_mean')
ax.legend(loc='upper right')

plt.show()

# window=3 の移動平均なので最初2つの行は NaN になっている
df_small = df_small.dropna()
print(mean_absolute_error(
    df_small_14['sales'][2:], df_small['rolling_mean_3']))
