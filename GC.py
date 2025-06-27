'''
#Problem: Given DNA Sequences, calculate the GC content of each and plot it as a histogram'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
data = {
    "GeneID": [f"G{i}" for i in range(1, 16)],
    "Sequence": [
        "ATGCGTAA", "GGGCGCGT", "ATATATAT", "CGCGATAT",
        "GCGTGCAT", "TTATTATA", "CCGGCCGG", "GATCGATC",
        "TATATATA", "GCGCGCGC", "ATGCATGC", "GGATCCGG",
        "CATCATGG", "TGCATGCA", "GGTACCGA"
    ]
}
df = pd.DataFrame(data)
def calculate_gc(seq):
    gc = seq.count('G') + seq.count('C')
    return (gc / len(seq)) * 100 if seq else 0
df['GC_Content'] = df['Sequence'].apply(calculate_gc)
plt.figure(figsize=(9, 6))
plt.hist(df['GC_Content'], bins=6, color='hotpink', edgecolor='purple')
plt.title('GC Content Distribution Across Genes')
plt.xlabel('GC Content (%)')
plt.ylabel('Number of Sequences')
plt.grid(True)
plt.tight_layout()
plt.show()
