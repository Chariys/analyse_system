# -*- coding: utf-8 -*- 
# @Author : yunze
import xlrd
import pymysql



# db = pymysql.connect('你的ip', 'root', '数据库密码', '数据库名', charset='utf8')
data = xlrd.open_workbook("test.xls")
sheet = data.sheet_by_name("Sheet1")

db = pymysql.connect('127.0.0.1', 'root', 'root', 'analyze', port=3306, charset='utf8')
cur = db.cursor()

# # # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(1, sheet.nrows):
    normal = sheet.cell(r, 0).value
    origin = sheet.cell(r, 1).value
    flat = sheet.cell(r, 2).value
    company = sheet.cell(r, 3).value
    unit = sheet.cell(r, 4).value
    Intended = sheet.cell(r, 5).value
    types = sheet.cell(r, 6).value
    # sql = "insert into data (normal,origin,flat,company,unit,Intended,types) values(''''''%s'''''', ''''''%s'''''',''''''%s'''''', ''''''%s'''''',''''''%s'''''',''''''%s'''''',''''''%s'''''')"
    # values = [repr(normal), repr(origin), repr(flat), repr(company), repr(unit), repr(Intended), repr(types)]
    query = "INSERT INTO data(normal,origin,flat,company,unit,Intended,types) VALUES (''''''%s'''''',''''''%s'''''',''''''%s'''''',''''''%s'''''',''''''%s'''''',''''''%s'''''',''''''%s'''''')"%(normal, origin, flat, company,  unit,Intended,types)
    # 执行sql语句
    cur.execute(query)
cur.close()
db.commit()
db.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")

