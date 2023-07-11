import smtplib

my_email = "jiaq230526@gmail.com"
password = "###"

# s288-1-1-1 连接到google的邮箱服务，，这里是smtp.gmail.com
# 不同邮箱的地址不同
with smtplib.SMTP("smtp.gmail.com") as connection:
    # s288-1-1-2 对发送的内容加密
    connection.starttls()
    # s288-1-1-3 使用邮箱地址的密码登录邮箱
    # 目前google的安全设置没有找到，所以登陆不上
    connection.login(user=my_email,password=password)
    # s288-1-1-4 要发送的内容，以及收件人
    connection.sendmail(
        from_addr=my_email,
        to_addrs="qiooozhang55@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
