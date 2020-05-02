import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """2012/05/02"""
        output = """2013/01/01"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2020/05/02"""
        output = """2020/05/02"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2088/02/28"""
        output = """2088/02/29"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

import datetime

def resolve():
    YMD = input()
    loop = True
    while loop:
        date = datetime.datetime.strptime(YMD, '%Y/%m/%d')
        Y, M, D = map(int, YMD.split('/'))
        res1 = divmod(Y, M)
        if res1[1] or divmod(res1[0], D)[1]:
            YMD = (date + datetime.timedelta(days=1)).strftime('%Y/%m/%d')
        else:
            loop = False

    print(YMD)
