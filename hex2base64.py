


f = open('string.txt' ,'r')
for c in f.readlines():
	Str = c.strip()
	result = Str.decode("hex").encode("base64")
	print result

	





