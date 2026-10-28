
line_number = 0
file = open("data.txt", "r") 
longest_line = ""
line_number = 0 

for i, line in enumerate(file, start=1): 
    if len(line) > len(longest_line): 
        longest_line = line 
        line_number = i 

file.close() 

print("the longest line is:", longest_line.strip(), "and its line number is:", line_number)
