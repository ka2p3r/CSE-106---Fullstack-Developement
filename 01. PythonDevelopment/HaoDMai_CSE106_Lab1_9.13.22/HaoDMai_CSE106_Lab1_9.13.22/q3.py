word = input('Please enter the word\n')
word = word.lower()
ans = 0
with open('PythonSummary.txt', 'r') as f:
    for line in f:
        l = line.split()
        for item in l:
            item = item.lower()
            if item == word:
                ans+=1
                continue
            cmp = ''
            for ch in item:
                if ch.isalpha():
                    cmp+=ch
                else:
                    cmp=''

                if cmp == word:
                    ans+=1

    print(f'The word {word} occurs {ans} times')
