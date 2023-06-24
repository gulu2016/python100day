import pandas

#s226-1-1-1 使用pandas读取数据，并打印temp列
data = pandas.read_csv("data.csv")
print(data['temp'])

