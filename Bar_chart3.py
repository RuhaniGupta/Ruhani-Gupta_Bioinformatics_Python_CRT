'''Write a python program to count how many genes belong to each family from the given data and visualize
using bar chart'''
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
genes = [
    {"name": "Gene1", "family": "A"},
    {"name": "Gene2", "family": "B"},
    {"name": "Gene3", "family": "A"},
    {"name": "Gene4", "family": "C"},
    {"name": "Gene5", "family": "B"},
    {"name": "Gene6", "family": "A"},
    {"name": "Gene7", "family": "C"},
    {"name": "Gene8", "family": "B"},
]
family_counts = Counter(gene['family'] for gene in genes)
families = list(family_counts.keys())
counts = list(family_counts.values())
plt.figure(figsize=(8, 5))
plt.bar(families, counts, color='grey')
plt.title('Gene Count per Family')
plt.xlabel('Gene Family')
plt.ylabel('Number of Genes')
plt.grid(axis='y',linestyle='--')
plt.tight_layout()
plt.show()