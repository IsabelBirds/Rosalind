#Problem

#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#Return: A consensus string and profile matrix for the collection. 
# (If several possible consensus strings exist, then you may return any one of them.)

#Open fasta
filename = 'Bioinformatics_stronghold/CONS.txt'

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

# Make matrix

def consensus(fasta):
    order = ['A','C','G','T']
    #get occurences
    length = len(list(fasta.values())[0])
    A = [0] *  length
    C = [0] *  length
    G = [0] *  length
    T = [0] *  length
    for value in fasta.values():
        for i in range(0, length):
            if value[i] == 'A':
                A[i] += 1
            if value[i] == 'G':
                G[i] += 1
            if value[i] == 'C':
                C[i] += 1
            if value[i] == 'T':
                T[i] += 1
    matrix = [A, C, G, T]
    #most common at each position
    con_seq = ''
    for i in range(0, length):
        column = []
        for row in matrix:
            column.append(row[i])
        con_seq += order[column.index(max(column))]
    matrix = [con_seq, A, C, G, T]
    return(matrix)


Con_fastas = consensus(fastas)

print(Con_fastas[0])
print('A:',' '.join(map(str,Con_fastas[1])))
print('C:',' '.join(map(str,Con_fastas[2])))
print('G:',' '.join(map(str,Con_fastas[3]))) 
print('T:',' '.join(map(str,Con_fastas[4])))