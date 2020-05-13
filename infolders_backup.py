import os
import shutil

inputpath='everything before the structure comes in'
outputpath='structure comes after'

for path, dirs, files in os.walk(os.getcwd()):
    for dir in dirs:
        if dir=='this' or dir=='folder':
            for a, _, c in os.walk(os.path.join(path,dir)):
                for cc in c:
                    frompath=os.path.join(a,cc)
                    structure=os.path.join(outputpath, a[len(inputpath):])
                    os.makedirs(structure, exist_ok=True)
                    shutil.copy(frompath, structure)
    print('Finished')                    
