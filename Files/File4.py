# WRITING TO A FILE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

file_name = 'Test_File\PROGRAMMING.txt'

with open(file_name,'w') as file_object: # SAME LOGIC IN C !!! WE OPENNED FOR WRITING MEANS EDITING !!!!!
    file_object.write('I love programming.')

with open(file_name,'w') as file_object:  # IF I OPEN A FILE EXIST WITH 'w' MOD, INFO IN FILE WILL BE ERASED !!!!!!
    file_object.write(str(5))             # IF I WERE TO WRITE !!! file_object.write(5) !!! It would cause error
                                          # PYTHON ONLY WRITES STR TO TEXT FILES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# read mode (r), write mode(w), append mode(a), or for read and write (r+) SAME LOGIC IN C !!!!!

with open(file_name,'w') as file_object:
    file_object.write('I love programming.\n')  # WRITE STATEMENTS APPEAR ON THE SAME LINE !!! WE USE '\n' !!!
    file_object.write('I love creating new games.\n')

# APPENDING TO A FILE
# 'a' MOD APPEND NEW INFO TO FILE WITHOUT ERASING OLD DATA
file_name = 'Test_File\PROGRAMMING.txt'

with open(file_name,'a') as file_object:
    file_object.write('I also love datasets.\n')
    file_object.write('I love also love apps.\n')







