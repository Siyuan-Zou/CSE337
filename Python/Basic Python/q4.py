import codecs

#Part1
f ='q4text.txt'
f2 = 'blob.txt'
def nlp(filename, n):
    n_dict = dict()
    with codecs.open(filename, 'r', encoding='utf8') as theFile:
        #Remove \n\r from file, then filter out the '' from the list
        file_str_arr = list(filter(lambda x:x!='', theFile.read().replace('\r\n', '').split(' ')))
        i = 0
        while i < len(file_str_arr)-n+1:
            gram = ' '.join(file_str_arr[i:i + n])
            if gram in n_dict:
                n_dict[gram] += 1
            else:
                n_dict[gram] = 0
            i+=1
        return n_dict

#Part2
result = nlp(f2,3)
grams = list(result.keys())
print(grams)
for x in range(0,10):
    longestLengthKey =''
    for key in grams:
        if len(key) > len(longestLengthKey):
            longestLengthKey=key
    if longestLengthKey in grams:
        grams.remove(longestLengthKey)

    print(longestLengthKey)