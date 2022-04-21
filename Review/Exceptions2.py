file_name = 'Alice.txt'

# with open(file_name) as f_obj: WE'LL GET ERROR MESSAGE !!! FileNotFoundError !!!
    #contents = f_obj.read()

try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except:
    print("Sorry, the file " + file_name + " does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print("The file consist of " + str(num_words))



