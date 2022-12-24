# -*- coding: utf-8 -*-
'''
This implements: http://en.wikipedia.org/wiki/Inverted_index of 28/07/10
'''

from pprint import pprint as pp
from glob import glob
try: reduce
except: from functools import reduce
try:    raw_input #python 2
except: raw_input = input #python3


def parsetexts(fileglob='*.txt'):
    texts, words = {}, set()
    for txtfile in glob(fileglob):
        with open(txtfile, 'r') as f:
            txt = f.read().split()
            words |= set(txt)
            texts[txtfile.split('\\')[-1]] = txt
    return texts, words

def termsearch(terms): # Searches simple inverted index
    return reduce(set.intersection,
                  (invindex[term] for term in terms),
                  set(texts.keys()))

archivo = open('salida/salida.txt',"w")
texts, words = parsetexts()
#print('\nTexts')
#pp(texts)
#print('\nWords')
#pp(sorted(words))

invindex = {word:set(txt
                        for txt, wrds in texts.items() if word in wrds)
            for word in words}
print('\nInverted Index')
#pp({k:sorted(v) for k,v in invindex.items()})
#for k,v in invindex.items():
indice = invindex.items()
orden = sorted(indice)
print (orden)
for k,v in orden:
    print (str(k)+','+str(v))
    a =(str(k)+','+str(v)+'\n')
    archivo.write(a)
 #   print(str(k)+','+str(v))
  #  {k:sorted(v)}
    #print(v)
    
#print({k:sorted(v) for k,v in invindex.items()})

#cadena = 'preuba'
#print (cadena)
#print (invindex)
#terms = ["what", "is", "it"]
#print('\nTerm Search for: ' + repr(terms))
#pp(sorted(termsearch(terms)))
#archivo.write(cadena)  # escritura de los datos
archivo.close()