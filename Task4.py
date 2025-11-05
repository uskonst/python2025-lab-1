true = sum(float(x)<-5 for x in open('s.txt'))
ln = sum(float(x)<=0 for x in open('s.txt'))
print(f'{true*100/ln}%[{RED}{' '*true}{END}{'-'*(ln-true)}]')