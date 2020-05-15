import os
import shutil
import hashlib


inputpath = 'C:\\Users\\YC774\\test_move_files_py'
outputpath = 'C:\\Users\\YC774\\move_to'

file_str=['.txt', '.pub', '.doc', '.docx']

for dirpath, dirnames, filenames in os.walk(os.getcwd()):#you can replace the path

    for filen in filenames:
        print()
        if os.path.splitext(filen)[1] in file_str or (filen.endswith('.mat') and filen.startswith('SC')):
            structure = outputpath + '\\' + dirpath[len(os.getcwd()):] #you can replace the path. I was using cwd only for testing
            structure_file = structure + '\\' + filen
            

            if os.path.exists(structure_file):
            
                structure_file_read=open(structure_file).read()
                structure_file_id=hashlib.sha256(structure_file_read.encode('utf-8')).hexdigest()
                
                original_read=open(dirpath + '\\' + filen).read()
                original_id=hashlib.sha256(original_read.encode('utf-8')).hexdigest()

                if structure_file_id!=original_id:
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
                        nameYourFile=input('please type out a new valid file name: ')
                        newFile=structure + '\\' + nameYourFile + '.txt'
                        os.makedirs(structure, exist_ok=True)
                        shutil.copyfile(dirpath + '\\' + filen, newFile)

                
            os.makedirs(structure, exist_ok=True)
            print(dirpath + '\\' + filen)
            print(structure)
            shutil.copy(dirpath + '\\' + filen, structure)
print('test done')


            

   
