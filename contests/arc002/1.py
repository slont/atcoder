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
        input = """1001"""
        output = """NO"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2012"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2100"""
        output = """NO"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """2000"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    Y = int(input())
    print('YES' if not Y % 400 else ('NO' if not Y % 100 else ('YES' if not Y % 4 else 'NO')))
