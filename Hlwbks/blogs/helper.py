import hashlib

from Hlwbks.settings import SECRET_KEY


def set_password(password):
    # 密码加密
    for _ in range(1000):
        pwd = "{}{}".format(password, SECRET_KEY)
        h = hashlib.md5(pwd.encode('utf-8'))
        password = h.hexdigest()
    return password


def json_msg(code, msg=None, data=None):
    """封装json消息,code: 0为正确,其他为错误"""
    return {"code": code, "errmsg": msg, "data": data}
