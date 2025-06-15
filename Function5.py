def find_matches(query,db,list):
    match=[seq_id for seq_id,seq in db.items() if query in seq]
    return match


db = {
  "seq001": "ATGCGGAATT",
  "seq002": "CGTACGTAGC",
  "seq003": "TTATGCATTA",
  "seq004": "GGAATCCGTA",
  "seq005": "CATGCCGTAGC",
  "seq006": "GGGCGTGCAT",
  "seq007": "AATGCTAGCTA",
  "seq008": "CGCGATGCGC",
  "seq009": "TATATATATA",
  "seq010": "ATGCGGATGCA"
}
query="ATGC"
match_seq=find_matches(query,db,list)
print(match_seq)