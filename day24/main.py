# s219-1-1-1 使用with打开文件，可以自动关闭文件而不用手动调用close函数
# s219-1-1-2 调用close 函数可以节省资源
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# s219-1-1-3 mode的默认参数是"r"，只读的
# 如果改为"w"表示覆盖写
# 如果改为"a"表示追加写
# s219-1-1-4 只有"w"模式下才会向一个不存在的文件中写入数据
with open("my_file.txt",mode="a") as file:
    file.write("\nNew text")