from sklearn.metrics import mean_absolute_error
import pandas as pd
import matplotlib.pyplot as plt
from neuralprophet import NeuralProphet

# データセットの準備
df = pd.read_csv('data/train.csv')
df1 = df.query('store==1 & item == 1')
df1 = df1.drop(["store", "item"], axis=1)
df1 = df1.rename(columns={"date": "ds", "sales": "y"})

# データセットの分割
train = df1[:-365]  # 2013-2016年の販売実績
test = df1[-365:]  # 2017年の販売実績

# 機械学習モデルのインスタンス作成
m = NeuralProphet(seasonality_mode='multiplicative')

# validationの設定(3:1) & モデルのトレーニング
metrics = m.fit(train, freq="D")

# 作ったモデルで 2017 年の Sales を予測（train データの先 365 日分を予測）
future = m.make_future_dataframe(train, periods=365)
forecast = m.predict(future)

# 予測結果を test のデータフレームに追加
test["pred"] = forecast["yhat1"].to_list()

# MAEで精度を確認
print('MAE(NeuralProphet):')
print(mean_absolute_error(test['y'], test['pred']))

# 可視化
test.plot(title='Forecast evaluation', ylim=[0, 50])
plt.show()
