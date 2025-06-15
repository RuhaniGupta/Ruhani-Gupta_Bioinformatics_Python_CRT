db = {
  "ATGT":"geneA",  # 3/4 = 75%
  "ATGC":"geneB",  # 4/4 = 100%
  "TTAC":"geneC",  # 1/4 = 25%
  "ATGG":"geneD",  # 3/4 = 75%
  "ATCC":"geneD",  # 3/4 = 75%
  "AGGC":"geneF",  # 2/4 = 50%
}
def generate_report(dna,db):
    Count_G=0
    Count_C=0
    if dna in db:
        ID=db[dna]
    for i in dna:
        Count_G=dna.count(i)
        Count_c=dna.count(i)
    GC_Count=(Count_G+Count_C)/len(dna)*100
    if(GC_Count>=80):
        Status="Good Match"
    elif(GC_Count>=50 and GC_Count<80):
        Status="Moderate"
    else:
        Status="Poor Match"
    print(f"ID:{ID}|Match:{GC_Count}%|Status:{Status}")
Sequence="ATGT"
generate_report(Sequence,db)

#