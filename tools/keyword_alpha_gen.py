def keyword_alphabet(keyword:str,defaultAlphabet="abcdefghijklmnopqrstuvwxyz"):
    genned_alpha = ""
    occurances = []
    for char in (keyword + defaultAlphabet):
        if not char in occurances:
            occurances.append(char)
            genned_alpha += char
    
    return genned_alpha
    
