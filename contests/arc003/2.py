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
        input = """5
chokudai
kensho
imos
yuichirw
ao"""
        output = """chokudai
ao
kensho
imos
yuichirw"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
dart
art"""
        output = """art
dart"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    N = int(input())
    s = [input()[::-1] for i in range(N)]
    s.sort()
    res = [ss[::-1] for ss in s]
    for ss in res:
        print(ss)
