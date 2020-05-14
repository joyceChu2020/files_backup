import os
import shutil
import hashlib


inputpath = 'C:\\Users\\YC774\\test_move_files_py'
outputpath = 'C:\\Users\\YC774\\move_to'

file_str=['.txt', '.pub', '.doc', '.docx']

for dirpath, dirnames, filenames in os.walk(os.getcwd()):#you can replace the path

    for filen in filenames:
        print()
        if os.path.splitext(filen)[1] in file_str or (filen.endswith('.mat') and filen.startswith('SC'))
            structure = outputpath + '\\' + dirpath[len(os.getcwd()):] #you can replace the path. I was using cwd only for testing
            structure_file = structure + '\\' + filen
            

            if os.path.exists(structure_file):
            
                def checkid(somefile):
                    sha256=hashlib.sha256()
                    sha256.update(somefile.encode('utf-8'))
                    return sha256.hexdigest()

                if checkid(structure_file)!=checkid(dirpath + '\\' + filen):
                    print(structure_file)
                    whatToDo=input("The file you are trying to back up has the same name than the existing one.\nIf you want to replace the existing file (which has different content), please type Y.\n Otherwise (where I'm only assuming you want to rename the file name), please type N \n Then press ENTER: ")
                    if whatToDo == 'Y':
                        os.makedirs(structure, exist_ok=True)
                        print(structure)
                        shutil.copy(dirpath + '\\' + filen, structure)
                    if whatToDo == 'N':
                        nameYourFile=input('please type out a new valid file name: ')
                        newFile=structure + '\\' + nameYourFile + '.txt'
                        os.makedirs(structure, exist_ok=True)
                        shutil.copyfile(dirpath + '\\' + filen, newFile)

                
            os.makedirs(structure, exist_ok=True)
            print(dirpath + '\\' + filen)
            print(structure)
            shutil.copy(dirpath + '\\' + filen, structure)
print('test done')


            

   
