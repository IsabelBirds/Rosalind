#Problem
#A common substring of a collection of strings is a substring of every member of the collection. 
# We say that a common substring is a longest common substring if there does not exist a longer common substring. 
# For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, 
# "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

#Note that the longest common substring is not necessarily unique; for a simple example, 
# "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

#Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

#Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

#Open fasta
filename = 'Bioinformatics_stronghold/LCSM.txt'

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
print(fastas)



#for i in range(len(s)):
#   if s[i:].startswith(t):
#      print (i+1)