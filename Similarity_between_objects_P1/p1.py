# given n objects find and rank similar between them
import pandas as pd 

# find similarity between objects  and print 10 most similar objects without using any library
# 1. find similarity between objects
# 2. rank them
# 3. print 10 most similar objects

  
# readinag given csv file
# and creating dataframe
# dataframe1 = pd.read_csv("animal.txt")
  
# # storing this dataframe in a csv file
# dataframe1.to_csv('animal.csv', 
#                   index = None)
df=pd.read_csv('Similarity_between_objects_P1/animal.txt')
print(df)

similarity = []
for i in range(len(df)):
    for j in range(len(df)):
        if i != j:
            score = 0
            for k in range(1, len(df.columns)):
                a = df.iloc[i][k]
                b = df.iloc[j][k]
                # if a in nan or b in nan then convert it to 0
                if a != a:
                    a = 0
                if b != b:
                    b = 0
                var = a-b
                score += var*var
            score = score**0.5
            similarity.append([df['animal'][i], df['animal'][j],score])

#sort and print 10 most similar objects
similarity.sort(key=lambda x: x[2], reverse=False)
#print in tabular form
print(pd.DataFrame(similarity[:10], columns=['animal1', 'animal2', 'score']))