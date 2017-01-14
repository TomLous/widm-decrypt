import sys
import binascii
import operator


def main():
    # Afl 2 WIDM code on wall

    decodedString = ""

    #cypherText = "HXvfWs@4$#&Rty Pkm!nm348LgM**% GfrZ33?/?Rtc96"
    cypherText = "HXvfW5@4$#&RtyPkm!nm348LgM**%GfrZ33?/?Rtc96"

    # 44 chars

    # Tried:
    # Not base64 (invalid chars)
    # Not ROT47

    asciiNums = []
    charCount = {}

    print "char\tasciidec"
    for c in cypherText:
        asciiNum = ord(c)
        if c in charCount:
            charCount[c]+=1
        else:
            charCount[c] = 1
        asciiNums.append(asciiNum)
        print c,"\t\t",asciiNum



    print "asciiNums: min val: ",min(asciiNums), " max val: ",max(asciiNums), " range: ",max(asciiNums) - min(asciiNums)
    print charCount
    print sorted(charCount.items(), key=operator.itemgetter(1), reverse=True)

    # Clearly this is not a substitution cypher to few similar characters (3: 3's, 2: *'s, etc)






main()