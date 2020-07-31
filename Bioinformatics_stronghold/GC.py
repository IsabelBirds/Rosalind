#Problem
#The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. F
# or example, the GC-content of "AGCTATAG" is 37.5%. 

#In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", 
# where "xxxx" denotes a four-digit code between 0000 and 9999.

#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see 
# the note on absolute error below

filename = 'Bioinformatics_stronghold/GC.txt'

#Get IDs from fasta
def get_ids(filename):
    ids = []
    with open(filename,"r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                ids.append(line)
    return(ids)

IDs = get_ids(filename)
print(IDs)

#Open fasta
filename = 'Bioinformatics_stronghold/GC.txt'

def open_fasta(fasta_file):
    with open(fasta_file,"r") as f:
        # Create variables for storing the identifiers and the sequence.
        id = None
        seq = ''
        fasta = {}
        for line in f:
            line = line.strip()  # Remove trailing newline characters.
            if line.startswith(">"):
                if id is None:
                    # This only happens when the first line of the FASTA file is parsed.
                    id = line
                else:
                    # This happens every time a new FASTA record is encountered.
                    # Reinitialise the identifier and sequence variables to build up a new record.
                    id = line
                    seq = ''
            else:
                # This happens every time a sequence line is encountered.
                seq = seq + line
                fasta[id] = seq
    return(fasta)

fastas = (open_fasta(filename))

for key, value in fastas.items():
    print(key, value)

#Calculate GC content

def GC(fasta):
    GC_content = {}
    for key, value in fasta.items():
        GC_content[key] = ((value.count('C') + value.count('G')) / len(value)) * 100
    return(GC_content)

GC = (GC(fastas))
print(GC)

#Get highest content, assumes there is one "answer"

print(max(GC),GC[max(GC)])