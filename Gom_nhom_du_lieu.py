import pandas as pd
df = pd.read_excel("D://Diemthi.xlsx").head(11)
#Gom nhóm Toán
Toan = df["Toan"]
print("Điểm môn Toán: ",Toan)
#Gom nhóm Lý
Ly = df["Ly"]
print("Điểm môn Lý: ",Ly)
#Gom nhóm Hóa
Hoa = df["Hoa"]
print("Điểm môn Hóa: ",Hoa)
#Gom nhóm Anh
Anh = df["Anh"]
print("Điểm môn Anh: ",Anh)
