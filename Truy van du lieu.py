import pandas as pd
df = pd.read_excel("D://Diemthi.xlsx")
#Tính trung binh môn Toán
Toan = df["Toan"].mean()
print("Điểm TB môn Toán: ",Toan)
#Tính trung binh môn Lý
Ly = df["Ly"].mean()
print("Điểm TB môn Lý: ",Ly)
#Tính trung binh môn Hóa
Hoa = df["Hoa"].mean()
print("Điểm TB môn Hóa: ",Hoa)
#Tính trung binh môn Anh
Anh = df["Anh"].mean()
print("Điểm TB môn Anh: ",Anh)