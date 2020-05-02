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
        input = """34
ABABAAABACDDDABADFFABABDABFAAABFAA"""
        output = """2.7941176470588234"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
FFFFF"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    N = int(input())
    r = input()
    ac, bc, cc, dc = map(int, [r.count('A'), r.count('B'), r.count('C'), r.count('D')])
    print((4 * ac + 3 * bc + 2 * cc + dc) / N)
