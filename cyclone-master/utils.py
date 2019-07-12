# coding=utf-8
def str_to_bool(str):
    return True if str.lower() == 'true' else False


class Message:
    def __init__(self, m="", c=0):
        self.message = m
        self.code = c