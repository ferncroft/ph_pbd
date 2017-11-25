
import unittest

from mapper import get_commit
from reducer import get_timeofday, get_dayofweek

class TestCommits(unittest.TestCase):
    inline = 'r1551925 | Thomas | 2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015) | 1 line Changed paths:'
    
    def test_commit(self):
        commits = get_commit(inline)
        self.assertEqual('r1551925', commits.get('revision'))
        self.assertEqual('Thomas', commits.get('author'))
        self.assertEqual('2015-11-27', commits.get('date'))
        self.assertEqual('16:57:44', commits.get('time'))
        self.assertEqual('1', commits.get('number_of_lines'))

    def test_timeofday(self):
        self.assertEqual('E', 18)

    def test_dayofweek(self):
        self.assertEqual('Monday', get_dayofweek(1))

if __name__ == '__main__':
    unittest.main()
