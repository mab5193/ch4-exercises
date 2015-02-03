#Processing DNA in a file

file = open("input.txt") #open input of file
output = open("trimmed.txt","w") #open the output of file
for dna in file: #loop for each line
	trimmed_dna = dna[14:] #start at 15th character 
	output.write(trimmed_dna) #print sequence
	print("Processed sequence with length " + str(len(trimmed_dna))) #print to screen