# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:31:58 2020

@author: Kevin(Mingkun) Wang
"""

import unittest

class ThirtySecondsFormatter(object):
    def __init__(self):
        self= self
        
    def separation(self,double):
        integer = int(double)               #Get the number before the decimal point
        decimals = double % integer         #Get the number after the decimal point
        return integer,decimals
    
    def string_conversion(self,integer,decimals):
        thirty_two = decimals*32                    # Convert the decimal into 32nd dollar convention
        if integer <10:                     
            string_int = "0"+str(integer)           # Check and add padding 0
        else:
            string_int = str(integer)
        if thirty_two <10:
            string_dec = "0"+str(int(thirty_two))   # Check and add padding 0
        else:
            string_dec = str(int(thirty_two))
        return string_int+"-"+string_dec            # Return it in the correct format
    
    def formatter(self,double):
        integer, decimals = self.separation(double) #Combine two helper functions together
        return self.string_conversion(integer,decimals)
        
        
        
        
        
class UnitTest(unittest.TestCase):

    def test_separation(self):
        thirty_two_formatter = ThirtySecondsFormatter()
        self.assertEqual(thirty_two_formatter.separation(105.25),(105,0.25),'incorrect separation result') # Should separate into two numbers, one integer and one decimal
        
    def test_conversion(self):
        thirty_two_formatter = ThirtySecondsFormatter()
        self.assertEqual(thirty_two_formatter.string_conversion(105,0.25),"105-08","incorrect conversion result") # Should convert number into correct format

    def test_formatter(self):
        thirty_two_formatter = ThirtySecondsFormatter()
        self.assertEqual(thirty_two_formatter.formatter(9.75),"09-24","incorrect output") #Should deliver the correct format





if __name__ == '__main__':
    unittest.main()