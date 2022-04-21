from csv import reader

file_dir = "Test_File\input.txt"
infile = open(file_dir,"r")
f = open(file_dir, "r")
print(f.readline())
print(f.readline())
infile.close()
f = open(file_dir, "r")
for x in f:
    print(x)
infile.close()
f = open(file_dir, "r")
for x in f:
    x = x.rstrip()
    print(x)
infile.close()



