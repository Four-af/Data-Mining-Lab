#Write a program to display the frequency of word in ascending order in given text file

#Read and write and write a file content in python
file1 = open("practice.txt", "r")

print()

#creating a dictonary
dictionary = dict()


#iterating thru each line in text para
for line in file1:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word[len(word)-1] < 'a' or word[len(word)-1] > 'z':
            word = word.rstrip(word[-1])
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1

for key in list(dictionary.keys()):
    print(key, "\t:\t", dictionary[key])
        

    