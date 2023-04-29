import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp Excel
df = pd.read_excel('D://Diemthi.xlsx').head(6)

# Tạo biểu đồ cột
plt.bar(df['SBD'], df['Toan'])

# Đặt tên cho trục x và trục y
plt.xlabel('SBD')
plt.ylabel('Điểm Toán')

# Hiển thị biểu đồ
plt.show()

