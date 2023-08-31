import pandas as pd
import numpy as np
from itertools import combinations

df = pd.read_csv("Apriori_Algorithm_P4/dataset.csv", header=None)

candidate_set = []
frequent_set = []
items = pd.unique(df.values.ravel('K')) #traversing the df values in order they occur in memory(k)
items = items[~pd.isnull(items)]

#take minimum support from the user
min_support = int(input("+ Enter absolute value of minimum support:"))

for i in range(1,len(items)): 
    count = {}
    in_Process = []

    if i==1:
        candidate_set.append(items)
        for txn in candidate_set[i-1]:
            ctr=0
            for val in df.values:
                if txn in val:
                    ctr+=1
            count[txn] = ctr
    else:
        candidate_set.append(list(combinations(np.unique(np.array(frequent_set[i-2]).ravel('K')),i)))
        for txn in candidate_set[i-1]:
            ctr = 0
            for val in df.values:
                if all(i in val for i in txn):
                    ctr+=1
            count[txn] = ctr

    for k in count.keys():
        if count[k]>=min_support:
            in_Process.append(k)

    if in_Process == []:
        print("+ Frequency Set +", frequent_set)
        break

    frequent_set.append(in_Process)
