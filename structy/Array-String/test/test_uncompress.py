import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from uncompress import uncompress

class TestUncompress (unittest.TestCase):

    def test_case1(self):
        self.assertEqual(uncompress('3a2b1c'), 'aaabbc')
        self.assertEqual(uncompress('2a3b4c'), 'aabbbcccc')
        self.assertEqual(uncompress('5a'), 'aaaaa')
        self.assertEqual(uncompress('15a'), 'aaaaaaaaaaaaaaa')
        self.assertEqual(uncompress('1z2y3x'), 'zyyxxx')


    
if __name__ == '__main__':
    unittest.main()