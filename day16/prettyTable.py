from prettytable import PrettyTable

#s148-1-1-1 创建PrettyTable对象
table = PrettyTable()

#s148-1-1-2 创建table
table.add_column("name",["pakaqiu","jienigui","xiaohuolong"])
table.add_column("type",["dian","shui","huo"])

#s148-1-1-3 右边对齐
table.align = "r"

print(table)