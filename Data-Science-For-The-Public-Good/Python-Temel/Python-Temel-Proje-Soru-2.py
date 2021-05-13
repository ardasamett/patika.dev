
# Samet Arda Erdoğan | sametarda.dev@gmail.com

a = [[1, 2], [3, 4], [5, 6, 7]]


if isinstance(a[0], list): # 2-D
    a.reverse()
    for i in a:
        i.reverse()
else: # 1-D
    a.reverse()
    
print(a)