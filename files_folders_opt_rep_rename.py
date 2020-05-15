import os
import shutil
import hashlib

inputpath = 'file_path that you want to backup from'
outputpath = 'path that you want to send to'

file_str=['.raw', '.dcsraw', '.bin', '.txt', '.pdf', '.doc', '.docx']

for dirpath, dirnames, filenames in os.walk(inputpath):#you can replace the path
    for filen in filenames:
        if os.path.splitext(filen)[1] in file_str or (filen.endswith('.mat') and filen.startswith('SC')):
            structure = outputpath + '\\' + dirpath[len(inputpath):] #you can replace the path. I was using cwd only for testing
            structure_file = structure + '\\' + filen
            
            if os.path.exists(structure_file):
                structure_file_read=open(structure_file).read()
                structure_file_id=hashlib.sha256(structure_file_read.encode('utf-8')).hexdigest()
                original_read=open(dirpath + '\\' + filen).read()
                original_id=hashlib.sha256(original_read.encode('utf-8')).hexdigest()

                if structure_file_id != original_id:
                    print(structure_file_id)
                    print(original_id)
                    print(structure_file)
                    print(dirpath + '\\' + filen)
                    whatToDo=input("The file you are trying to back up has the same name than the existing one.\nIf you want to replace the existing file (which has different content), please type Y.\nOtherwise (where I'm only assuming you want to rename the file name), please type N \nThen press ENTER: ")

                    if whatToDo == 'Y':
                        os.makedirs(structure, exist_ok=True)
                        print(structure)
                        shutil.copy(dirpath + '\\' + filen, structure)

                    if whatToDo == 'N':
                        nameYourFile=input('please type out a new valid file name with extention: ')
                        newFile=structure + '\\' + nameYourFile
                        create_newFile=open(newFile, 'w')
                        create_newFile.close()
                        shutil.copyfile(dirpath + '\\' + filen, create_newFile)

            os.makedirs(structure, exist_ok=True)
            print(dirpath + '\\' + filen)
            print(structure)
            shutil.copy(dirpath + '\\' + filen, structure)

    for dirn in dirnames:
        if dirn=='DICOM_ScanDirs' or dirn=='Finapres':
            for a, _, c in os.walk(os.path.join(path, dirn)):
                for cc in c:
                    frompath = os.path.join(a, cc)
                    structure = outputpath + '\\' + a[len(inputpath):]
                    structure_file = structure + '\\' + cc

                    if os.path.exists(structure_file):
                        structure_file_read=open(structure_file).read()
                        structure_file_id=hashlib.sha256(structure_file_read.encode('utf-8')).hexdigest()
                        frompath_read=open(frompath).read()
                        frompath_id=hashlib.sha256(frompath_read.encode('utf-8')).hexdigest()

                        if structure_file_id != frompath_id:
                            print(structure_file_id)
                            print(frompath_id)
                            print(structure_file)   
                            print(frompath)
                            whatToDo=input("The file you are trying to back up has the same name than the existing one.\nIf you want to replace the existing file (which has different content), please type Y.\nOtherwise (where I'm only assuming you want to rename the file name), please type N \nThen press ENTER: ")

                            if whatToDo == 'Y':
                                os.makedirs(structure, exist_ok=True)
                                print(structure)
                                shutil.copy(frompath, structure)

                            if whatToDo == 'N':
                                nameYourFile=input('please type out a new valid file name with your extention: ')
                                newFile=structure + '\\' + nameYourFile
                                create_newFile=open(newFile, 'w')
                                create_newFile.close()
                                shutil.copyfile(dirpath + '\\' + filen, newFile)

                    os.makedirs(structure, exist_os=True)
                    shutil.copy(frompath, structure)
print('test done')
