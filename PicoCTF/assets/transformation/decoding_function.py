encoded_flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽"
	

decoded_string = []
for i in range(0,len(encoded_flag),1) :
	
	first_decoded_character = chr(ord(encoded_flag[i]) >> 8)
	decoded_string.append(first_decoded_character)
	
	second_decoded_character = chr(ord(encoded_flag[i]) - (ord(first_decoded_character) << 8))
	decoded_string.append(second_decoded_character)
	
print(''.join(decoded_string))
	 
