#!/usr/bin/env python3

import unittest
from shapes import Triangle

class TestTriangle(unittest.TestCase): 
    #def setUp(self):
    #    self.a_triangle = Triangle('Ted')

    def testShapeType(self): 
        self.assertEqual(Triangle.shape_type, 'Triangle')

    #def testArea(self):
    #    self.assertEqual(Triangle.area, )
    def testPerimeter(self):
        self.assertEqual(Triangle.perimeter, 3*2)
    
if __name__=='__main__':
    unittest.main()

