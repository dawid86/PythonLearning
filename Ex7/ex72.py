# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values
# from each of the lines and compute the average of those values
# and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fhand = open(fname)
linecount = 0
totalvalue = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        linecount = linecount + 1
#        print(totalvalue)
        totalvalue = float(line[line.find(":")+1:len(line)].rstrip()) + totalvalue
#        print(line)
#        print(totalvalue)
#print("Done","number of lines",linecount, totalvalue, totalvalue/linecount)
print("Average spam confidence:",totalvalue/linecount)
