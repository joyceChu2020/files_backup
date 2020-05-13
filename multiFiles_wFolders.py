import os
import shutil

inputpath = 'Y:\\hypercapnia'
outputpath = 'C:\\Users\\me\\backup\\hypercapnia'

file_str=['.raw', '.dcsraw', '.bin', '.txt', '.pdf', '.doc', '.docx']

for dirpath, dirnames, filenames in os.walk(inputpath):
    for filen in filenames:
        if os.path.splitext(filen)[1] in file_str or (filen.endswith('.mat') and filen.startswith('SC')):
            structure = outputpath + dirpath[len(inputpath):]
            os.makedirs(structure, exist_ok=True)
            shutil.copy(os.path.join(dirpath, filen), structure)
            
    for dirn in dirnames,
        if dirn=='This' or dirn=='That':
            for a, _, c in os.walk(os.path.join(path, dirn)):
                for cc in c:
                    frompath = os.path.join(a, cc)
                    structure = outputpath + a[len(inputpath):]
                    os.makedirs(structure, exist_os=True)
                    shutil.copy(frompath, structure)
