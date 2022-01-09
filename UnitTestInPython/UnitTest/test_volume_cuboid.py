"""
Created on Fri Jan 07 20:53:58 2022
@author: Ankit Bharti

"""


from unittest import TestCase, main
from cuboid_volume import *


class TestCuboid(TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2), 8)
        self.assertAlmostEqual(cuboid_volume(1), 1)
        self.assertAlmostEqual(cuboid_volume(0), 0)

    def test_input_value(self):
        self.assertRaises(TypeError, cuboid_volume, 'ank')

    def test_addition(self):
        self.assertEqual(add(3, 4), 7)
        self.assertAlmostEqual(add(4.5, 6.2), 10.701, places=2)

    def test_addition_input_value(self):
        self.assertRaises(TypeError, add, 'ank', 6)


if __name__ == '__main__':
    main()
