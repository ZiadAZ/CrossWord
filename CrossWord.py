import random


class CrossWord:

    def __init__(self, size):
        self.size = size
        self.questions = []
        self.gride = []
        
    def addWord(self, info):
        word = info.word
        if len(word) > self.size: return False

        if len(self.gride) == 0 and len(word) == self.size:
            self.gride = list(word)

            self.questions.append('   [{0}] [{1}] to [{2}] [{3}] '.format(
                0, 0, 0, len(word))+info.question)
        elif self.gride.__contains__(word[0]):
            index = self.gride.index(word[0])

            if self.gride[index] is not list:
               self.gride[index] = list(word)
               self.questions.append('   [{0}] [{1}] to [{2}] [{3}] '.format(
                   0, index, len(word), index)+info.question)




'''        self.gride=[*range(size)]
        for i in self.gride:
          self.gride[i]=[*range(size)]
'''

   

'''
   def addRandomWord(self,info):
        
        rand = lambda x:random.randrange(x)
        size=self.size
        vertical=rand(2)%2==0
        for i in info:
            print(type(i))
            word=i.word
            const=rand(size)
            print(const)
            wl=len(word)
            if wl>size :return
            if vertical:
              self.gride.insert([0][0],word)
              self.questions.append('   [{0}] [{1}] to [{2}] [{3}] '.format(0,const,wl,const)+i.question)
            else :
               self.gride.insert([const][0],[const][wl],word) 
               self.questions.append('   [{0}] [{1}] to [{2}] [{3}] '.format(const,0,const,wl)+i.question)

 #   def fillRandomWord(self,*info):
        
        
      
              
      '''                
