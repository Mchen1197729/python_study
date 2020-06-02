import re

print(re.match(r'\d+\w$', '1a'))

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

# 切分字符串
string = 'a b   c'
print(str.split(string, ' '))
print(string.split(' '))
print(re.split(r'\s+', string))

# 如果一个正则表达式需要使用多次 可以进行预编译 以避免每次使用都进行编译
phone_reg = re.compile(r'^(\d{3})\-(\d{3,8})$')

print(phone_reg.match('010-45567').groups())
print(phone_reg.match('010-4556890').groups())
print(re.match(phone_reg, '010-4556890').groups())

print('**************************')


def is_valid_email(addr):
    email_reg = re.compile(r'^\w+\.?\w+\@\w+(\.com)$')
    return email_reg.match(addr)


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
