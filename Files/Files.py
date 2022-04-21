# READING FROM A FILE
print("1-\n")
with open('PI.txt') as file_object:
    contents = file_object.read()  # THESE MUST BE LIE UNDER THE WITH OPEN... !!!!!
    print(contents)
    print(contents.rstrip())  # rstrip() removes whitepsace or blank stripes right side of the file !!!!!

# IF OUR FILE IS NOT CONTAINED WITH THE OUR PYTHON FILE OPENING THE TARGET FILE !!!!!!!!!!!!!!!!!!!!
print("\n2-\n")

with open('Test_File\PI.txt') as file_object: # IN WINDOWS WE USE '\' INSTEAD OF '/' !!!!!
    contents = file_object.read()  # THESE MUST BE LIE UNDER THE WITH OPEN... !!!!!
    print(contents)
print("\n3-\n")
file_path = 'Test_File\PI.txt'    # I CAN ASSIGN FILE PATH TO A VARIABLE !!!!!
with open(file_path) as file_object:
    contents = file_object.read()  # THESE MUST BE LIE UNDER THE WITH OPEN... !!!!!
    print(contents)





