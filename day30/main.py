# s269-1-1-1 处理异常，try一定会执行
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["key"])
# s269-1-1-2 except会在有异常时候执行，多个except处理不同的异常
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} doex not exist.")
# s269-1-1-3 else会在没有异常的时候执行
else:
    content = file.read()
    print(content)
# s269-1-1-4 finally都会执行，执行清理资源，关闭文件之类的操作
finally:
    file.close()
    print("File was closed")