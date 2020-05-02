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
        input = """7 34"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """19 28"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    M = '0123212332'
    A, B = map(int, input().split(' '))
    res1 = divmod(abs(B - A), 10)
    print(res1[0] + int(M[res1[1]]))
