# Use words.txt as the file name
# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

fname = input("Enter file name: ")
fhand = open(fname)
# fread = fhand.read()
# print(fread.upper())
#for line in fread:
#    line = line.rstrip()
#    line = fread.upper()
#    print(line)
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)
