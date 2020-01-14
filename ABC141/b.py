S=input()

odd=S[0::2]
even=S[1::2]

if 'L' in odd:
    print('No')
elif 'R' in even:
    print('No')
else:
    print('Yes')