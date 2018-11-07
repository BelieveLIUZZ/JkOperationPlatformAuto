
"""
0,adminer,123456,登录成功
1,adminer,000000,密码校验错误
2,admin,123456,账号不存在
3,admin,666666,账号不存在
4,,,
"""


class LoginFunction:

    def login_function(self, username, password):
        if username == 'adminer' and password == '123456':
            return '登录成功'
        elif username == 'adminer' and password == '000000':
            return '密码错误'
        elif username == 'admin' and password == '123456':
            return '用户名错误'
        elif username == 'admin' and password == '666666':
            return '用户名错误'


