from datetime import datetime

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>文件读写 file-like Object>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    # >>>open for read...
    print(s)
    # >>>今天是 2021-01-06

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    # >>>open as binary for read...
    print(s)
    # >>>b'\xbd\xf1\xcc\xec\xca\xc7 2021-01-06'
    print('byte encode by GBK is', str(s, encoding="GBK"))
    # >>>byte encode by GBK is 今天是 2021-01-06
