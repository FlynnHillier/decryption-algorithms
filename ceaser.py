def ceaserChiper(text:str, **kwargs):
    args = {
        "shift":-1,
        "decrypt":False
    }
    args.update(kwargs)
    alpha = "abcdefghijklmnopqrstuvwxyz"

    if args["shift"] != -1:
        shifts = [args["shift"]] 
    else:
        shifts = list(range(1,len(alpha)))


    for shift in shifts:
        decipheredText = ""
        for key in text.lower():
            alphaIndex = alpha.find(key)
            if(alphaIndex == -1):
                decipheredText += key
                continue

            decipheredText += alpha[(alphaIndex + (shift * (-1 if args["decrypt"] == True else 1))) % len(alpha)]
        print(f"{'encrypt' if args['decrypt'] == False else 'decrypt'}ion mode, {shift} character shift:")
        print(decipheredText)