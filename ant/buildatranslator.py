def translator(phrase):
    translation = ""
    for letter in phrase:
       if letter.upper() in "AIOEU" :
           if letter.islower() :
                translation = translation + "g"
           else:
                translation = translation + "G"
       else:
           translation = translation + letter

    return translation

print(translator(input("input a phrase :")))
