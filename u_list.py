def sublist_by_index(li, indices, index_start=0):
    """
    ===========================================================================
     Description: Return Sublist based on requested indices.
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. li : list (Source List).
        2. indices : list of int (List of Requested Indices).
        3. index_start : int (From which index the Source Lists starts).
    ===========================================================================
     Return: list (Sublist of Source List based on requested indices).
    ===========================================================================
    """
    sub = list()
    for index in indices:
        index -= index_start
        sub.append(li[index])
    return sub
    
    
"""
===============================================================================
===============================================================================
=========================  Tester  ============================================
===============================================================================
===============================================================================
"""
def tester():
    
    import u_tester
   
    def tester_sublist_by_index():        
        
        # Simple Test
        li = ['a','b','c']
        indices = [0,2]
        li_test = sublist_by_index(li,indices)
        li_true = ['a','c']
        p1 = li_test == li_true
        
        # Test with index_start (like from Excel)
        li = ['a','b','c']
        indices = [1,2]
        li_test = sublist_by_index(li,indices,index_start=1)
        li_true = ['a','b']
        p2 = li_test == li_true
        
        u_tester.run([p1,p2])
            
    
    print('\n====================\nStart Tester\n====================')    
    tester_sublist_by_index()
    print('====================\nEnd Tester\n====================')            
    
#tester()            