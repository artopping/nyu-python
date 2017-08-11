#!/usr/bin/env python3

import unittest
from classes import Triangle

class TestTriangle(unittest.TestCase): 
    def setUp(self):
        self.a_triangle = Triangle('Ted')
        #self.allies= ['Circle']

    def testAllies (self):
        value= self.a_triangle.add_ally('Square')
        allies= ['Circle']
        self.assertNotEqual (allies,value)    
    
    def testShapeType(self): 
        self.assertEqual(Triangle.shape_type, 'Triangle')

    def testPerimeter(self):
        self.assertEqual(self.a_triangle.perimeter(), (3*2))

    def testArea (self):
        self.assertNotEqual(self.a_triangle.area(), 0)
   
if __name__=='__main__':
    unittest.main()

