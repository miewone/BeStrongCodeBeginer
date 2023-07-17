word = int(input())
word_list = []
for i in range(word):
    word_list.append(input())
set_word = list (set(word_list))

sort_word = []
for i in set_word:
    sort_word.append((len(i),i))
result = sorted(sort_word)
for len_word, word in result: 
    print(word)
