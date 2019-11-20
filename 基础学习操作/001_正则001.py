import re

def is_valid_email(addr):
    custom1 = re.compile(r'[\w\.]+@\w+\.com')
    if custom1.match(addr):
        return True







# 测试:
# assert is_valid_email('gmail.c@someon.cn')
assert is_valid_email('someone@gmail.com')
# assert is_valid_email('some...one@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')