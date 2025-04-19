
import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('实验后原.xlsx', sheet_name='Sheet1')
df_1 = pd.read_excel('实验后等效.xlsx')


# 提取 U_data
U_data = []
# 提取 I_data
I_data = []

# 遍历每一行数据
for index,row in df.iterrows():
    if 'V(2)' in row['Variable, Parameter setting']:
        U_data.append(row['Operating point value'])
    else:
        if 'I(RL)' in row['Variable, Parameter setting']:
            I_data.append(row['Operating point value'])




# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签SimHei
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

plt.plot(I_data, U_data)



# 添加标题和标签

plt.title('U-I特性曲线')
plt.xlabel('电流//A')
plt.ylabel('电压//V')

plt.show()




print(U_data)
print(I_data)