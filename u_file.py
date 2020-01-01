import os
import sys
import shutil
import fileinput
import u_str

def get_files_by_extension(path, extension):
    """
    ===========================================================================
     Description: Return List of FilePaths with all files in the path with
                     the specified extension (deep traverse).
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path : str (Path where to search).
        2. extension : str (File Extension, e.g 'txt').
    ===========================================================================
     Return: list of str (List of FilePaths with specified extension).
    ===========================================================================
    """
    extension = '.' + extension    
    li = list()
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                full_path = u_str.get_full_path(path,file)
                li.append(full_path)
    return li


def get_files_names(path):
    """
    ===========================================================================
     Description: Return List of Files Names in the Path.
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path : str (Path where to search).
    ===========================================================================
     Return: list of str (List of Files Names).
    ===========================================================================
    """
    names = list()
    for name in os.listdir(path):
        full_path = u_str.get_path(path,name)
        if os.path.isfile(full_path):
            names.append(name)
    return names


def move_file(path_src, path_dest):
    """
    ===========================================================================
     Description: Move file from src to dest.
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path_src : str (Path to Source File).
        2. path_dest : str (Path where to move the file).
    ===========================================================================
    """
    shutil.copyfile(path_src, path_dest)
    
    
def move_files(path_src, path_dest):
    """
    ===========================================================================
     Description: Move all Files from Source Dir to Destination Dir.
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path_src : str (Path to Source Directory).
        2. path_dest : str (Path to Destination Directory).
    ===========================================================================
    """
    names = get_files_names(path_src)
    for name in names:
        path_src = u_str.get_path(path_src,name)
        path_dest = u_str.get_path(path_dest,name)
        move_file(path_src, path_dest)
    
    
def replace_in_file(path, tuples):
    """
    ===========================================================================
     Description: Replace string in File.
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path : str (Path of File to change).
        2. tuples : list of tuples (Every Tuple contains what_replace and
                        with_replace, e.g ('a','o')).
    ===========================================================================
    """
    for t in tuples:
        what_replace = t[0]
        with_replace = t[1]
        for line in fileinput.input(path, inplace=1):                    
            sys.stdout.write(line.replace(what_replace,with_replace))
            
            
def path_to_filename(path, with_domain=True):
    """
    ===========================================================================
     Description: Extract FileName from the Path (with or without domain).
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path : str (FullPath of the FileName).
        2. with_domain : bool (Domain is for example .txt or .py).
    ===========================================================================
     Return: str (FileName extracted from the FullPath).
    ===========================================================================
    """  
    vals = path.split('\\')
    filename = vals[-1]
    if not with_domain:
        vals = filename.split('.')
        filename = '.'.join(vals[:-1])
    return filename


def bi_gram(path_1, path_2):
    def get_words(path):
        words = list()
        file = open(path,'r')
        for line in file:
            words.extend(line.split())
        file.close()
        return words
    
    def get_tuples(words):
        tuples = set()
        for i in range(len(words)-2):
            tuples.add((words[i],words[i+1],words[i+2]))
        return tuples
    
    words_1 = get_words(path_1)
    tuples_1 = get_tuples(words_1)
    
    words_2 = get_words(path_2)
    tuples_2 = get_tuples(words_2)
        
    count_intersection = len(set.intersection(tuples_1,tuples_2))
    count_union = len(set.union(tuples_1,tuples_2))
    size_min = min(len(words_1),len(words_2))
    size_max = max(len(words_1),len(words_2))
    size = size_min / size_max   
    
    print(tuples_1-tuples_2)
    
    return round((count_intersection / count_union)*size,2)


"""
===============================================================================
===============================================================================
=========================  Tester  ============================================
===============================================================================
===============================================================================
"""
def tester():
    
    import u_tester            
        
    def tester_path_to_filename():
        
        path = 'c:\\test\\file.name.py'
        
        # With Domain
        filename_test = path_to_filename(path)
        filename_true = 'file.name.py'
        p1 = filename_test == filename_true
        
        # Without Domain
        filename_test = path_to_filename(path,with_domain=False)
        filename_true = 'file.name'
        p2 = filename_test == filename_true
        
        u_tester.run([p1,p2])
                
    
    print('\n====================\nStart Tester\n====================')    
    tester_path_to_filename()
    print('====================\nEnd Tester\n====================')        
    
    
tester() 