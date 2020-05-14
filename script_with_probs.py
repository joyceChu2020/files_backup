import os
import shutil
import hashlib


inputpath = 'Y:\\hypercapnia'

outputpath = 'C:\\Users\\me\\backup\\hypercapnia\\'



file_str=['.raw', '.dcsraw', '.bin', '.txt', '.pdf', '.doc', '.docx']



for dirpath, dirnames, filenames in os.walk(inputpath):

    for filen in filenames:

        if os.path.splitext(filen)[1] in file_str or (filen.endswith('.mat') and filen.startswith('SC')):

            structure = outputpath + '\\' + dirpath[len(inputpath):]
            structure_file = structure + '\\' + filen

            if os.path.exists(structure_file):
                structure_file_hash = hashlib.sha256()
                readSize=65556
                with open(structure_file, 'rb') as f:
                    fb = f.read(readSize)
                    while len(fb)>0:
                        structure_file_hash.update(fb)
                        fb=f.read(readSize)
                structure_file_id=structure_file_hash.hexdigest()
                
                file_hash = hashlib.sha256()
                with open(os.path.join(dirpath, filen), 'rb') as f:
                    fb = f.read(readSize)
                    while len(fb)>0:
                        file_hash.update(fb)
                        fb=f.read(readSize)
                file_id = file_hash.hexdigest()

                if structure_file_id == file_id:
                    next(filenames)
                else:
                    whatToDo=input("The file you are trying to back up has the same name than the existing one.\n If you want to replace the existing file (which has different content), please type Y. \n Otherwise (where I'm only assuming you want to rename the file name), please type N \n Then press ENTER")
                    if whatToDo == 'Y':
                        os.makedirs(structure, exist_ok=True)
                        shutil.copy(os.path.join(dirpath, filen), structure)
                    if whatToDo == 'N':
                        nameYourFile=input('please type out a new valid file name:')
                        newFile=structure + '\\' + nameYourFile + '\\' + '.txt'
                        os.makedirs(newFile, exist_ok=True)
                        shutil.copyfile(os.path.join(dirpath, filen), newFile)

            else:
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
