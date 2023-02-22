file1 = open("RandJ.txt", 'r')
wordfile = file1.read().splitlines()
file1.close()
accumulate = [0]*20
for word in wordfile:
    accumulate[int(len(word))]= accumulate[int(len(word))]+1
for i in range(1,20):
    print("there were ", accumulate[i], "words of length ", i)

