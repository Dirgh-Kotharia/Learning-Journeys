encoded_flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽"
	

decoded_string = []
for i in range(0,len(encoded_flag),1) :
	
	first_decoded_character = chr(ord(encoded_flag[i]) >> 8)
## shifting the binary value right will return us the orginal first character since when binary right shift happens,
## the moved bits are dropped.
## eg : 1794 in binary would be 11100000010 and if it is right shifted 8 bit we will get 111 which is 7 in decimal
##      and if we take 1799 it will be 11100000111 and after 8 bit right shift we will get 111 which is 7 in decimal
	decoded_string.append(first_decoded_character)
	
	second_decoded_character = chr(ord(encoded_flag[i]) - (ord(first_decoded_character) << 8))
## Subtracting the integer value of decoded character we get the second character. we are jsut reversing the operation 
## we did during encoding 
##  encoding we did :  
##	   encoded_flag[i] = chr((ord(first_decoded_character) << 8) + ord(second_decoded_character))
## ==> ord(encoded_flag[i]) = (ord(first_decoded_character) << 8) + ord(second_decoded_character) bcs ord() and chr () are reverse function
## ==> ord(encoded_flag[i]) - (ord(first_decoded_character) << 8) = ord(second_decoded_character)
## ==> chr(ord(encoded_flag[i]) - (ord(first_decoded_character) << 8)) = second_decoded_character
	decoded_string.append(second_decoded_character)
	
print(''.join(decoded_string))
	 
