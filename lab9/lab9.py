import urllib
import urllib.request
import requests
import re

PhoneticAna = {}
 
def soundexNaive(name, len=4):
    sndx = name[0] #Keep the first letter

    for i in name[1:]:
        if i in "BFPV":
           d = "1"
        elif i in "CGJKQSXZ":
            d = "2"
        elif i in "DT":
            d = "3"
        elif i in "L":
            d = "4"
        elif i in "MN":
            d = "5"
        elif i == "R":
            d = "6"
        else:
            d = ""

        if d != sndx[-1]:
            sndx += d
    return (sndx + (len * '0'))[:len]

def soundex(name, len = 4):
    digits = '01230120022455012623010202'

    #retain first letter of string
    sndx = name[0]

    #translate each successive letter in name
    for c in name[1:]:
        d = digits[ord(c)-ord('A')]

        #if 2+ letters with same number are adjacent then just keep 1
        if d != '0' and d != sndx[-1]:
            sndx += d

    #remove all 0s from soundex code
    sndx = sndx.replace('0',"")
    return(sndx + (len*'0'))[:len]


def metaphone(name):

    RULES = [ 
        # Regexp, replacement
        [ r'([bcdfhjklmnpqrstvwxyz])\1+',r'\1' ],# Remove doubled consonants except g.
        [ '^ae',            'E' ], # ae -> E
        [ '^[gkp]n',        'N' ], # initial kn-, gn-, pn- -> N
        [ '^wr',            'R' ], # initial wr- -> R
        [ '^x',             'S' ], # x- -> S
        [ '^wh',            'W' ], # initial wh- -> W
        [ 'mb$',            'M' ], # -mb (as in dumb) -> M
        [ '(?!^)sch',      'SK' ], # sch -> SK
        [ 'th',             '0' ], # 0 represents the th sound
        [ 't?ch|sh',        'X' ], # tch, tsh, ch, sh -> X
        [ 'c(?=ia)',        'X' ], # cia -> X
        [ '[st](?=i[ao])',  'X' ], # stia, stio -> X
        [ 's?c(?=[iey])',   'S' ], # ci, ce, cy, sci, sce, scy -> S
        [ '[cq]',           'K' ], # c, q -> K
        [ 'dg(?=[iey])',    'J' ], # dgi, dge, dgy -> J (as in ledger, edgy)
        [ 'd',              'T' ], # d -> T
        [ 'g(?=h[^aeiou])', ''  ], # gh -> silent (gh- not at end or before vowel)
        [ 'gn(ed)?',        'N' ], # gne, gnd -> N
        [ '([^g]|^)g(?=[iey])',r'\1J' ], # gi, ge, gy, but not gg -> J
        [ 'g+',             'K' ], # g, gg -> K (as in egg)
        [ 'ph',             'F' ], # ph -> F
        [ r'([aeiou])h(?=\b|[^aeiou])',r'\1' ], # silent h if after vowel and no following vowels
        [ '[wy](?![aeiou])', '' ], # wy is silent if not followed by vowel
        [ 'z',              'S' ], # z -> S
        [ 'v',              'F' ], # v -> F
        [ '(?!^)[aeiou]+',  ''  ], # vowels silent unless first letter
    ]

    # Normalise case and remove non-ASCII
    name = name.lower()
    s = re.sub('[^a-z]', '', name)
    # Apply the Metaphone rules
    for (rx, rep) in RULES:
        s = re.sub(rx, rep, s)
    return s.upper()    


def task13():

    user_in = input('Input name: ')
    print("soundexNaive: ", soundexNaive(user_in.upper()))
    print("soundex: ", soundex(user_in.upper()))
    print("metaphone: ", metaphone(user_in))

    

    #req = urllib2.Request('http://cs.brynmawr.edu/Courses/cs330/spring2017/soundex.txt')
    #response = urllib2.urlopen(req)
    #data = response.read()

def task4():
    link = "http://cs.brynmawr.edu/Courses/cs330/spring2017/FemaleNames2.txt"
    f = requests.get(link)
    data = f.text.split('\n')
    
    for line in data:
        print(line)
        
        p_key = soundex(line.upper())
        
        if p_key not in PhoneticAna:
            dict[p_key] = [line]
        else:
            dict[p_key].append(line)

        
def printDict():
    for k, v in PhoneticAna.items():
        if len(v) >= 2:
            s = ','
            print(k, end='\t')
            print(s.join(v))

            
#task4()
#printDict()
task13()
