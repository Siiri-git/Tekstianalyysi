import heapq
from collections import Counter

with open("artikkeli1.txt", 'r', encoding='utf-8') as file:
    content = file.read()
    wrds = content.split()
    

cnt = Counter(wrds)

k = 5
top_k = heapq.nlargest(k, cnt.items(), key=lambda x: x[1])
topWrds = []
for item in top_k:
    topWrds.append(item[0])
print(', '.join(topWrds))