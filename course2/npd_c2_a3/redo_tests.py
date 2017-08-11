#!/usr/bin/env python3

import unittest
from redo_classes import Triangle

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.a_triangle = Triangle('Ted')
    def testAllies (self):
        value= self.a_triangle.allies
        allies= ['Circle']
        self.assertEqual (allies,value)

    def testShapeType(self):
        self.assertEqual(self.a_triangle.shape_type, 'Triangle')

    def testUpdateEdgeLength(self):
        self.assertNotEqual(self.a_triangle.edge_length, self.a_triangle.update_edge_length(3))

    def testPerimeter(self):
        self.assertEqual(self.a_triangle.perimeter(), (3*2))

    def testArea (self):
        self.assertNotEqual(self.a_triangle.area(), 0)

if __name__=='__main__':
        unittest.main()
 

