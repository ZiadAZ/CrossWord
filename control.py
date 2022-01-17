from word import Word
from data import Words_list
from CrossWord import CrossWord


t = []
i = 0
for w, q in Words_list:

    w = Word(Id=i, word=Words_list[i].get(w), question=Words_list[i].get(q))
    t.append(w)
    i += 1


t.sort(key=len,)



crossWord = CrossWord(6)


def arr():

    for w in t:
        crossWord.addWord(w)


arr()
for row in crossWord.gride:

    print(row)

for row in crossWord.questions:

    print(row)
