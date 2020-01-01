import u_bool
import u_inspect
#import u_file

def run(predicates):    
    """
    ===========================================================================
     Description: Run tester function and print OK or FAILED.
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. predicates : list of bool (List of Tester Predicates).
    ===========================================================================
    """
    line = ': {0}'
    if u_bool.all(predicates):
        line = 'OK' + line
    else:
        line = 'Failed' + line
        
    called_method = u_inspect.called_method()
    len_tester = 7
    fname = called_method[len_tester:]
    print(line.format(fname))
    
    
def print_start(path_module):
    """
    ===========================================================================
     Description: Print Start Tester with the name of the tested Module.
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path_module : str (Path of the tested Module).
    ===========================================================================
    """
    name = path_module.split('\\')[-1].split('.')[0]
    print('\n{0}\nStart Tester: {1}\n{0}'.format('='*30,name))


def print_finish(path_module):
    """
    ===========================================================================
     Description: Print Finish Tester with the name of the tested Module.
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path_module : str (Path of the tested Module).
    ===========================================================================
    """
    name = path_module.split('\\')[-1].split('.')[0]
    print('{0}\nFinish Tester: {1}\n{0}'.format('='*30,name))
    
    
"""
===============================================================================
===============================================================================
=========================  Tester  ============================================
===============================================================================
===============================================================================
"""
def tester():
   
    def tester_run():
        run(True)
        run(False)            
    
    print('\n====================\nStart Tester\n====================')    
    tester_run()
    print('====================\nEnd Tester\n====================')            
    
#tester()
        
#print_start('stam')
#print_finish('stam')
