import binascii


def onlyascii(char):
    if ord(char) < 32 or ord(char) > 122: return ''
    else: return char



List = open("keywords.txt").read().splitlines()
with open("hex.txt") as f:
    for line in f:
    	hexin  = line
    	#print hexin
    	for k in range(0,255):
    		i =0
    		xxx = len(hexin)/2
    		s =""
    		for j in range(xxx):
    			abc = hexin[i] + hexin[i+1]
    			i = i+2
    			abc = "0x" +abc
    			result  = (int(abc,16) ^ k)

    			abc = str(chr(result))
    			abc =onlyascii(abc)
    			s = s+str(abc)
    			

    		
    		spl = s.split()
    		if len(spl) >= 3:
    			if  [(w,List.count(w)) for w in set(List) if w in spl] != []:
    				print s
    			
		

