import os

def get_filenames(folder):
    """
    ===========================================================================
     Description: Get List of FileNames in Folder (without domain).
    ---------------------------------------------------------------------------
        For Example Files in Folder: 1.txt, 2.txt, 3.txt
        Returns: ['1','2','3']
    ===========================================================================
     Arguments:
    ---------------------------------------------------------------------------
        1. folder : str (Path to the Folder).
    ===========================================================================
     Return: list of str (FileNames in Folder).
    ===========================================================================
    """
    li = os.listdir(folder)
    for i, file in enumerate(li):
        li[i] = li[i].partition('.')[0]
    return li