# s236-1-1-1 readlines读取文件，每行都变为content1中的1个元素
with open('file1.txt') as f1:
    content1 = f1.readlines()
print(content1)

with open('file2.txt') as f2:
    content2 = f2.readlines()
print(content2)

# s236-1-1-2 先判断该元素是否在另一个列表中，如果在的话，就把该元素转为int
result = [int(num) for num in content1 if num in content2]

print(result)