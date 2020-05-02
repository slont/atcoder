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
        input = """9
131142143"""
        output = """4 1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """20
12341234123412341234"""
        output = """5 5"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4
1111"""
        output = """4 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    input()
    c = input()
    res = [c.count('1'), c.count('2'), c.count('3'), c.count('4')]
    print(max(res), min(res))
