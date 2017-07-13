# this is an encrytion program
# * takes a input via text or file
# *encrypts the text
# *decryt back
# *print          :)

import getpasss
import numpy as np
from random import shuffle

def enhance(enpt,row,col,flag):
    key={}
    alphabet=list(map(chr,range(33,123)))
    numb=list(map(int,range(33,123)))
    shuffle(numb)
    numchar=[]
    for no in numb:
        numchar.append(chr(no))

    key=dict(zip(alphabet,numchar))
    if flag == True:
                print "\n\n*********************************************************\n"
                print "key \n ",key,
    count=-1
    eenpt=np.chararray((col,col))
    eenpt[:] = '*'
    for item in enpt:
        for word in item:
            if word == '*':
                count += 1
                continue
            try:
                count += 1
                eenpt.itemset(count,key.get(word))
            except IndexError:
                break
    if flag == True:
        print "\n\n*********************************************************\n"
        print "Enhanced matrix \n ",eenpt,
    return eenpt,key

def normal(eenpt,row,col,key,flag):
    data=''
    e_data=''
    count = -1
    ddept=np.chararray((col,col))
    ddept[:] = '*'
    rev_key=dict(zip(key.values(),key.keys()))
    for item in eenpt:
        for word in item:
            data = ''
            if word == '*':
                count += 1
                continue
            try:
                count += 1
                data = rev_key.get(word)
                ddept.itemset(count,data)
            except IndexError:
                break
    if flag == True:
        print "\n\n*********************************************************\n"
        print "Non-Enhanced matrix\n ",ddept,
    return ddept

def encrypt(s1,flag):
    index = []
    s=list(s1.strip())
    for word in s[:]:
        if word is ' ':
            index.append(s.index(word))
            s.remove(word)                                                      #get index
    l=len(s)
    row = int( l ** 0.5)
    col = row

    for i in xrange(100):
        if row*col >=l:
            break                                                                       #get row,column
        elif i%2 is 0:  col += 1
    else: row +=1
    text = np.chararray((col,col))
    text[:] = "*"
    enpt = np.chararray((col,col))
    enpt[:]="*"
    c=0
    for i in xrange(row):
        for j in xrange(col):
            try:                                                        #filling the matrix (text)
                text.itemset((i,j),s[c])
                c += 1
            except IndexError:
                break

    for i in xrange(col):
        for j in xrange(row):
            data=''
            data = text.item((j,i))
            enpt.itemset((i,j),data)                                           #print encrypt(transpose of text)
    data=' '

    if flag ==True:
        print "Encrypted matrix is \n",enpt
    eenpt,key=enhance(enpt,row,col,flag)

    for item in eenpt:
        for words in item:
            for word in words:
                if word is '*':
                    continue
                data += word                               #print encrypt in string type
    if flag == True:
        print "\n\n*********************************************************\n"
        print "ENCRYPTED TEXT DISPLAYED : >>>",
        print data,
    else :  print "Encypted Text:",data
    return eenpt,index,row,col,key

def decrypt(eenpt,index,row,col,key,flag):
    dept=np.chararray((col,col))
    dept[:]='*'

    ddept=normal(eenpt,row,col,key,flag)

    for i in xrange(col):
        for j in xrange(row):                                       #decrypt = original matrix
            data=''
            data=ddept.item((i,j))
            dept.itemset((j,i),data)
    sst=''
    for item in dept:
        for word in item:
            try:
                sst += word                                       #get decrypt matrix in string(str1)
            except UnboundLocalError:
                pass
    if flag == True:
        print "\n\n*********************************************************\n"
        print "Decrypted matrix \n",dept
    sttt=''
    prev_index=0
    for i in index:
        int_index=int(i)            #adding index spaces
        sttt += sst[prev_index:int_index]+' '
        prev_index = int_index
    sttt+=sst[prev_index:]
    decstr=''
    for i in sttt:
            if i == '*':
                continue
            decstr += i
    if flag == True:
        print "\n\n*********************************************************\n"
        print "DECRYPTED TEXT DISPLAYED : >>> ",decstr.strip(),
    else :  print "Decrypted Text:",decstr.strip()

def main():
    flag = False
    while True:
        print "\n\n*********************************************************\n"
        ii=raw_input("1 for filename. \n2 for text\n3 for exit>>> ")
        if ii == '3':
            break
        if ii == '1':
            print "enter ->>( # )<<-  to stop !!"
            fname=(raw_input("enter the file name:"))
            f=open(fname,'r')
            text=f.read()
            if text is '#' or fname is '#':
                break
            print "\n\n*********************************************************\n"
            f=raw_input('want to see the working (y/n): ')
            if f =='y':
                flag = True
            e,i,r,c,key=encrypt(text,flag)
            print "\n\n*********************************************************\n"
            d=raw_input("\n\nenter d to decrypt:>>>>>>>>> ")
            if d is 'd':
                decrypt(e,i,r,c,key,flag)
            continue
        else:
            text = ''
            print "enter ->>( # )<<-  to stop !!"
            text=getpasss.getpass(prompt='\nenter the text(it will not be displayed): ')
            if text is '#':
                break
            print "\n\n*********************************************************\n"
            f=raw_input('\nwant to see the working (y/n): ')
            if f =='y':
                flag = True

            e,i,r,c,key=encrypt(text,flag)
            print "\n\n*********************************************************\n"
            d=raw_input("\n\nenter d to decrypt: ")
            if d is 'd':
                decrypt(e,i,r,c,key,flag)

            print "\n\nprogram terminating...\nTerminated"

if __name__ == '__main__':
    main()
