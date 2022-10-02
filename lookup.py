import enchant

class Lookup:
    def __init__(self,depth=10,strict=0.4):
        self.dict = enchant.Dict("en_GB")
        self.depth = depth
        self.strict = strict

    
    def checkText(self,text:str,depth:int = -1,strict=-1):
        if depth <= 0:
            depth = self.depth

        if strict <= 0 or strict > 1:
            strict = self.strict
        

        checkWords = text.split(" ")[0::1]
        score = 0

        for word in checkWords:
            if self.checkWord(word):
                score += 1

        return [strict < (score / len(checkWords)),score / len(checkWords)]

    def checkWord(self,word:str):
        return self.dict.check(word)

    def filter(self,texts:list,depth:int = -1,strict:int =-1,sort:bool = True):
        if depth <= 0:
            depth = self.depth

        if strict <= 0 or strict > 1:
            strict = self.strict
        
        acceptedTexts = []

        for text in texts:
            [result,score] = self.checkText(text,depth=depth,strict=strict)
            if result == True:
                acceptedTexts.append({
                    "score":score,
                    "text":text
                })

        if sort == True:
            acceptedTexts = sorted(acceptedTexts, key = lambda d: d["score"],reverse=True)

        return acceptedTexts

    def list_Of_Dicts_To_Texts(self,listOfDicts:list,key:str):
        texts = []
        for d in listOfDicts:
            text = d.get(key,None)
            if text == None or not isinstance(text,str):
                continue
            texts.append(d[key])

        return texts









      
    

    