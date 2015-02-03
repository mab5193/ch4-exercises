#Multiple exons from genomic DNA

genomic_dna = open("genomic_dna.txt").read() #open file and read

exon_locations = open("exons.txt") #open exons file

coding_sequence = "" #create variable for coding coding sequence 

for line in exon_locations: #loop through exon locations file
	positions = line.split(',') #split with comma
	start = int(positions[0])
	stop = int(positions[1]) #start and stop positions
	exon = genomic_dna[start:stop] #extract exon 
	coding_sequence = coding_sequence + exon #attach exon 

output = open("coding_sequence.txt", "w") #write to output file
output.write(coding_sequence)
output.close()
