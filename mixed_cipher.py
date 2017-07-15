import sys 
import string 


plaintext='abcdefghijklmnopqrstuvwxyz'

abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z']

word= raw_input("Please enter a keyword for the mixed cipher:\n")

word=word.lower()

W=[]

for letter in word:
	if letter not in W:
	   W.append(letter)

keyWord=''.join(W)

for letter in keyWord:
	if letter in abc:
		abc.remove(letter)

abc = W + abc #cyphertxt  

alpha=''.join(abc)#cyphertxt list to string 

UP=plaintext.upper()

UA=alpha.upper()

U=string.maketrans(UP,UA)

ALPHA=string.maketrans(plaintext, alpha)

print "Plaintext:"+ plaintext 

print "Ciphertext:"+ alpha

#FILE MANP.

name = sys.argv[-1]

f= open(name, 'r')

s= f.read()

a= s.translate(ALPHA)

c= a.translate(U)

print c


































	
