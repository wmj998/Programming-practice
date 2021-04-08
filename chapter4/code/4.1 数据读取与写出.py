# 代码 4-1
import pandas as pd
df = pd.read_csv('D:/文件丶/课件/《Python机器学习编程与实战》源数据和代码/第4章/示例程序/data/meal_order_info.csv', encoding='gbk')
print('读取的CSV文件前5行数据为：\n', df.head())


# 代码 4-2
df1 = df.head()
df1.to_csv('D:/文件丶/课件/《Python机器学习编程与实战》源数据和代码/第4章/示例程序/tmp/meal_order_info_out.csv', encoding='gbk')
print('df1的前2行数据为：\n', df1.head(2))


# 代码 4-3
df = pd.read_excel('D:/文件丶/课件/《Python机器学习编程与实战》源数据和代码/第4章/示例程序/data/users_info.xlsx')
print('读取的Excel文件前5行数据为：\n', df.head())


# 代码 4-4
df1 = df.head()
df1.to_excel('D:/文件丶/课件/《Python机器学习编程与实战》源数据和代码/第4章/示例程序/tmp/users_info_out.xlsx')
print('df1的后2行数据为：\n', df1.tail(2))


# 代码 4-5
from sqlalchemy import create_engine
# 创建一个mysql连接器，用户名为root，密码为12345
# 地址为127.0.0.1，数据库名称为test_db，编码为utf-8
# 创建数据表orders
engine = create_engine(
        'mysql+pymysql:'
        '//root:12345@127.0.0.1:3306/test_db?charset=utf8mb4')
print(engine)


# 代码 4-6
orders = pd.read_sql('select * from orders', con=engine)
print('读取的数据表orders前5行数据为：\n', orders.head())


# 代码 4-7
df.to_sql('orders_out', con=engine, index=False)
orders_out = pd.read_sql('select * from orders_out', con=engine)
print('写入数据后数据表orders_out前5行数据为：\n', orders_out.head())
