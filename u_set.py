def get(s, item):
    """
    ===========================================================================
     Description: Return the Item from the Set (None if not exists).
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. s : set 
        2. item : item
    ===========================================================================
     Return: item (None if not exists).
    ===========================================================================
    """
    for x in s:
        if item == x:
            return x
    return None
    
    
"""
===============================================================================
===============================================================================
=========     Tester     ======================================================
===============================================================================
===============================================================================
"""

import u_tester

def tester():
    
    def tester_get():
        
        s = {1,2,3}
        item_test = u_set.get(s,2)
        p0 = item_test == 2
        
        item_test = u_set.get(s,5)
        p1 = item_test == None
        
        u_tester.run([p0,p1])
        
    
    u_tester.print_start(__file__)
    tester_get()
    u_tester.print_finish(__file__)
                
#tester()
                