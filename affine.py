from pydantic.utils import deep_update
from math import gcd,floor


def affine(plaintext:str,**kwargs):
    args = deep_update({
        "multi":{
            "range":{
                "max":16,
                "min":1
            },
            "static":-1,
        },
        "add":{
            "range":{
                "max":-1,
                "min":0
            },
            "static":-1,
        },
        "alphabet":"abcdefghijklmnopqrstuvwxyz",
        "decrypt":False
    },kwargs)

    decrypt = args["decrypt"]
    alphabet = args["alphabet"]
    results = []


    multiplicative_config = args["multi"]
    if multiplicative_config["static"] != -1: #use static value
        multipliers = [multiplicative_config["static"]]
    else: #use range
        min = multiplicative_config["range"]["min"]
        max = multiplicative_config["range"]["max"] + 1
        if min > max or min < 0 or max < 0:
            raise Exception(f"invalid addition range provided: [ min:{multiplicative_config['range']['min']} , max:{multiplicative_config['range']['max']} ]")

        multipliers = list(range(min,max))

    

    addititive_config = args["add"]
    if addititive_config["static"] != -1: #use static value
        adders = [addititive_config["static"]]
    else: #use range
        max = (addititive_config["range"]["max"] if addititive_config["range"]["max"] != -1 else len(alphabet)) + 1
        min = addititive_config["range"]["min"]
        if min > max or min < 0 or max < 0:
            raise Exception(f"invalid addition range provided: [ min:{multiplicative_config['range']['min']} , max:{multiplicative_config['range']['max']} ]")

        adders = list(range(min, max))


    invalid_multipliers = []

    for multiplier in multipliers:
        if not gcd(len(alphabet),multiplier) == 1: #is not coprime
            invalid_multipliers.append(multiplier)
            continue
        
        for adder in adders:
            out = ""
            for char in plaintext.lower():
                index = alphabet.find(char)
                if index == -1:
                    out += char
                    continue
                
                if decrypt == False:
                    out += alphabet[((index * multiplier) + adder) % len(alphabet)]
                else:
                    out += alphabet[int(((index - adder) / multiplier)) % len(alphabet)]

            results.append({"multiplier":multiplier,"addition":adder,"output":out,"decipher":decrypt})

    return results
    

