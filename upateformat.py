# -*- coding:utf-8 -*-



a=open('wordbook.txt','rb')


singleword=[]
outfile=open('myword.txt','wb')
numcount=1
for i in a:

    tmp=i.split('\t')
    for j in tmp:
        if j!='':

            singleword.append(j)

    singleword.insert(1,'  ')
    singleword.insert(0,str(numcount)+'. ')
    outfile.writelines(singleword)
    singleword=[]
    numcount+=1
outfile.close()
a.close()


