
name_list = ['aa', 'bb', 'cc', 'dd', 'ee']
addr_list = ['beijing', 'fujian', 'xinjiapo']
company_list = ['baidu', 'tengxun', 'advance']

import random
import time

def get_name():
    return name_list[random.randint(0, 4)]