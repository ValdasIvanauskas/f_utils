import os
import sys
import shutil
import fileinput
import u_str
import u_text_mining


def get_paths_by_extension(path, extension):
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
                full_path = '\\'.join([root,file])
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

    
def create_txt(path, lines=list()):
    """
    ===========================================================================
     Description: Create Text File from List of Lines (str + '\n').
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path : str (Path to Text File to create).
        2. lines : list of str (List of Lines str + '\n').
    ===========================================================================
    """
    file = open(path,'w')
    for line in lines:
        file.write(line + '\n')
    file.close()
    
    
def to_str(path):
    """
    ===========================================================================
     Description: Convert Text File into long str.
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path : str (Path to the Text File).
    ===========================================================================
    """
    file = open(path)
    ans = ''.join(file.readlines())
    file.close()
    return ans


def cosine_similarity(path_1, path_2):
    """
    ===========================================================================
     Description: Return Cosine Similarity between two text files.
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. path_1 : str (Path to the first File).
        2. path_2 : str (Path to the second File).
    ===========================================================================
     Return: float (Cosine Similarity between the two files).
    ===========================================================================
    """
    str_1 = to_str(path_1)
    str_2 = to_str(path_2)
    return u_text_mining.cosine_similarity(str_1, str_2)


"""
===============================================================================
===============================================================================
=========================  Tester  ============================================
===============================================================================
===============================================================================
"""
def tester():
    
    import u_tester       
    import u_dir     
        
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
        
    
    def tester_create_txt():
        
        path_dir = 'c:\\tester_create_txt'
        u_dir.create(path_dir)
        
        path_file = path_dir + '\\test.txt'
        
        line_1 = 'hello'
        line_2 = 'world'
        lines = [line_1, line_2]
        create_txt(path_file, lines)
        
        str_test = to_str(path_file)
        str_true = 'hello\nworld\n'
        
        u_dir.delete(path_dir)
        
        p0 = str_test == str_true
        
        u_tester.run([p0])
       
        
        
    def tester_to_str():
        
        path_dir = 'c:\\tester_to_list_words'
        u_dir.create(path_dir)
        
        line_1 = 'aaa\tbbb ccc'
        line_2 = 'ccc bbb aaa'
        lines = [line_1, line_2]
        
        path_file = path_dir + '\\test.txt'
        create_txt(path_file,lines)
        
        str_test = to_str(path_file)
        str_true = 'aaa\tbbb ccc\nccc bbb aaa\n'
        
        p0 = str_test == str_true
        
        u_dir.delete(path_dir)
        
        u_tester.run([p0])


    def tester_cosine_similarity():

        path_dir = 'c:\\tester_cosine_similarity'
        u_dir.create(path_dir)
        
        path_file_1 = path_dir + '\\test_1.txt'
        path_file_2 = path_dir + '\\test_2.txt'
        
        lines = ['hello world']
        create_txt(path_file_1,lines)
        create_txt(path_file_2,lines)
        
        p0 = cosine_similarity(path_file_1, path_file_2) >= 0.99
        
        u_dir.delete(path_dir) 
        
        u_tester.run([p0])
        
        
    def tester_get_paths_by_extension():
    
        path_dir = 'c:\\tester_get_paths_by_extensions'
        u_dir.create(path_dir)
        
        path_dir_1 = path_dir + '\\1'
        path_dir_2 = path_dir + '\\2'
        path_dir_11 = path_dir_1 + '\\11'
        u_dir.create(path_dir_1)
        u_dir.create(path_dir_2)
        u_dir.create(path_dir_11)
                
        path_file_1 = path_dir + '\\test_1.java'
        path_file_2 = path_dir + '\\test_2.java'
        path_file_3 = path_dir_1 + '\\test.java'
        path_file_4 = path_dir_2 + '\\test.java'
        path_file_5 = path_dir_11 + '\\test.java'

        create_txt(path_file_1)
        create_txt(path_file_2)
        create_txt(path_file_3)
        create_txt(path_file_4)
        create_txt(path_file_5)
        
        paths_test = get_paths_by_extension(path_dir, 'java')
        paths_true = [path_file_1, path_file_2, path_file_3, path_file_4, path_file_5] 
        
        u_dir.delete(path_dir)
        
        p0 = set(paths_test) == set(paths_true)
        
        u_tester.run([p0])
        
    
    u_tester.print_start(__file__)
    tester_path_to_filename()
    tester_create_txt()
    tester_to_str()
    tester_cosine_similarity()
    tester_get_paths_by_extension()
    u_tester.print_finish(__file__)        
    
    
tester() 