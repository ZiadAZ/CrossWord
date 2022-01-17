import random
class Word:
    
    
    def __str__(self):
      return (self.word)

    def __len__(self):
     return random.randrange(9999999)
 
    def   __init__(self,Id,word,question):
     self.Id=Id
     self.word=word
     self.question=question


    def __randomming__(self):
     return random.random(9999999)