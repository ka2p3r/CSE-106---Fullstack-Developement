sentence = input('Please enter the sentence\n')
times = int(input('Please enter the number of times\n'))

with open("CompletedPunishment.txt", 'a') as f:
    for i in range(times):
        f.write(sentence)
        f.write('\n')
