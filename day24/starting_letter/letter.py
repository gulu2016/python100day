# s223-1-1-1 letter模板中要替换的字符串
PLACEHOLDER = "[name]"

# s223-1-1-2 打开邀请名单，readlines会将读到的文件作为List返回，每个元素代表一行
with open("./invited_names.txt") as name_file:
    names = name_file.readlines()


with open("./letter_temp.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # s223-1-1-3 将名字后边的'\n'去掉
        stripped_name = name.strip()
        # s223-1-1-4 替换模板内容后，将内容写到新文件中
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
        with open(f"./output/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)
