import unittest     

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    if a+b>c and b+c>a and a+c>b:
        if a == b and b == c:
            return 'Equilateral'
        elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
            return 'Right'
        elif a == b or b == c or c == a:
            return 'Isoceles'
        else:
            return 'Scalene'
    else:
        return 'NotATriangle'
    
        
        


class TestTriangles(unittest.TestCase):
    def testSet1(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testMyTestSet2(self): 
        self.assertEqual(classifyTriangle(1,1,3),'NotATriangle','should be a notatrianle')
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','should be equilateral')
        self.assertEqual(classifyTriangle(21,22,30),'Scalene','Should be Isoceles')
        

if __name__ == '__main__':
    unittest.main(exit=False) 