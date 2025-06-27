def find_differences(seq1,seq2):
    if len(seq1)!=len(seq2):
        raise ValueError
    difference = [i for i in range (len(seq1)) if seq1[i] != seq2[i]]
print (difference)
                  
        
