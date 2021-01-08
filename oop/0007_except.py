# -*- coding: utf-8 -*-
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>错误 except & 打印 logging>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

import logging

logging.basicConfig(level=logging.DEBUG)


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except Exception as e:
        print('ValueError!')
        # logging.exception(e)
        raise


try:
    bar()
except Exception as e:
    print("ValueError...")
    logging.info("ValueError...")
finally:
    print("finally...")
    logging.debug("finally...")
