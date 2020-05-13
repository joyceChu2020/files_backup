import os
import shutil

inputpath = 'structure after inputpath would be saved'
outputpath = 'structure would be concatenated to this outputpath'

for dirpath, dirnames, filenames in os.walk(inputpath):
    for filen in filenames:
        if filen.endswith('.raw'):
            structure = os.path.join(outputpath, dirpath[len(inputpath):]) #if the join function messes things up then simply use'+'
            os.makedirs(structure, exist_ok=True)
            shutil.copy(os.path.join(dirpath, filen), structure)
    print('job is done!')
