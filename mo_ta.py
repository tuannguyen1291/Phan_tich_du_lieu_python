import pandas as pd
df = pd.read_excel("D://Diemthi.xlsx").head(11)
describe = df.describe()
print(describe)