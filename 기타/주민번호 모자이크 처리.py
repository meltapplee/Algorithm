data = '''
park 800905-1234567
kim  700905-2345678
'''

#result = []
#for line in data.split("\n"):
#    conv = []
#    for a in line.split():
#        if len(a) == 14 and a[:6].isdigit() and a[7:].isdigit():
#            a = a[:8] + '*' * 6
#        conv.append(a)
#    result.append(" ".join(conv))
#print("\n".join(result))

##------정규식에 의하여
import re
print('정규식에 의하여')
pat = re.compile(r"(\d{6})([-][1-4])\d{6}")
print(pat.sub("\g<1>\g<2>" + '*' * 10, data))