import unittest
import ex137p151

class Test_algos_tri(unittest.TestCase):

    def test_compare_tableaux(self):
        assert(ex137p151.compare_tableaux([1, 6, 3], [1, 6, 3]) is True)
        assert(ex137p151.compare_tableaux([1, 2, 3], [1, 6, 3]) is False)
        assert(ex137p151.compare_tableaux([1, 6, 3, 5], [1, 6, 3]) is False)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
