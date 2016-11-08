print "1st Hex String"
str1 =raw_input()

print "2nd Hex String"
str2 = raw_input()
str1 ="0x" +str1
str2 ="0x"+str2

str1 = int(str1 ,0) 
str2 =int(str2,0)
result = hex(str1 ^ str2)
print  result 

