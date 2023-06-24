# s233-1-1-1 将list中的数都+1并返回
num = [1,2,3]
new_number = [n+1 for n in num]
print(new_number)

# s233-1-1-2 对于str的内容同样适用于简易的for操作
name = "jiaqian"
letter_list = [letter for letter in name]
print(letter_list)

# s233-1-1-3 对于range，适用于简易的for操作
range_list = [num*2 for num in range(1,5)]
print(range_list)

# s233-1-1-4 可以在for循环中添加条件，只返回满足条件的item
names = ["aaa","bbbb","ccccc","dddddd"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(long_names)
