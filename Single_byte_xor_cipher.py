import binascii



List = open("keywords.txt").read().splitlines()
for k in range(0,128):
	hexin ="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	
	i =0
	xxx = len(hexin)/2
	s =""
	
	for j in range(xxx):
		abc = hexin[i] + hexin[i+1]
		i = i+2
		abc = "0x" +abc
		result  = (int(abc,16) ^ k)
		
		abc = str(unichr(result))
		s = s+str(abc)
	
	spl = s.split()
	
	if  [(w,List.count(w)) for w in set(List) if w in spl] != []:
		print s

