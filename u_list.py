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


def bigram(li):
    """
    ===========================================================================
     Description: Convert List into List of Tuples (BiGram method).
    ---------------------------------------------------------------------------
        1. list('abc') => [ tuple('ab'), tuple('bc') ]
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. li : list. 
    ===========================================================================
     Return: list of tuple (List of Tuples in BiGram method).
    ===========================================================================
    """
    tuples = list()
    if len(li)<2:
        return tuples
    for i in range(len(li)-1):
        tuples.append((li[i],li[i+1]))
    return tuples            

    
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
        
        
    def tester_bigram():
        
        li = list('abc')
        bigram_test = bigram(li)
        bigram_true = [ tuple('ab'), tuple('bc') ]
         
        p0 = bigram_test == bigram_true
        
        u_tester.run([p0])
        
        
    u_tester.print_start(__file__)
    tester_sublist_by_index()
    tester_bigram()
    u_tester.print_finish(__file__)            
    
#tester()            