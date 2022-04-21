# WORKING WITH MULTIPLE FILES

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file contains " + str(num_words) + " words.")

def count_words2(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass                        # PASS IS A NEW ARGUMENT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else:
        words = contents.split()
        num_words = len(words)
        print("The file contains " + str(num_words) + " words.")

filename = 'Test_File\Alice.txt'
count_words(filename)
print("")

# WORKING WITH MULTIPLE FILES !!!

filenames = ['Test_File\Alice.txt','Test_File\Siddartha.txt','Test_File\Moby_Dick.txt','Test_File\Little_Women.txt']

for filename in filenames:
    count_words(filename)

# PASS ARGUMENT LOOK AT THE FUNCTION 2 !!!

print("")

for filename in filenames:
    count_words2(filename)  # THE ERROR DOES NOT APPEAR !!!








