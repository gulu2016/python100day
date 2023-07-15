

# s307-1-1-1 define a func with parameter type and return type
def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    # s307-1-1-2 parameter type and return type only work as hint
    # it's not mandatory check, like below code will also work
    return "can_drive"
    # return can_drive

print(police_check(19))
# s307-1-1-3 if we input a str type, it will fail on line5,
# it will not check when it enter the police_check func
print(police_check("19"))