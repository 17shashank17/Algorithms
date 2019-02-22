def word_frquency(s,n):
    wordlist = s.split()

    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))
    wordlist1=list(set(wordlist))
    wordfreq1=list(set(wordfreq))
    print(wordlist1)
    list1=[]
    for i in range(n):
        max1=wordfreq1.index(max(wordfreq1))
        list1.append((wordlist1[max1],wordfreq1[max1]))
    return list1
s = "the the the quick quick brown brown brown brown fox jumps jumps over" 
print(word_frquency(s,2))