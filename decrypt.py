import sys
import binascii
import operator

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes


def main():
    # Afl 2 WIDM code on wall

    decodedString = ""

    #cypherText = "HXvfWs@4$#&Rty Pkm!nm348LgM**% GfrZ33?/?Rtc96"
    cypherText = "HXvfW5@40$#&RtyPkm!nm348LgM**%GfrZ33?/?Rtc96"


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

    primes = get_primes(len(cypherText))

    filtered = map(lambda p: cypherText[p-1], primes)

    print "".join(filtered)



    # pip install hashid
    # > unknown hash

    # Every sentence starts with capital letter (H,P,G)

    #maybe other puzzles
    # 6, 9 ,20 puzzle = 43
    # words:
    # geld - waarde
    # pakpapier - fabriek - joker
    # zwarte - test
    # schrijvers -  schrijven - schetsen
    # pen -etui
    # achterste - voorste -middelset
    # biografie





main()

