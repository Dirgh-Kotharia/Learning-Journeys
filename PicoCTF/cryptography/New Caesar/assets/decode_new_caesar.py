import string

ALPHABET = string.ascii_lowercase[:16]


def reverse_shift(original_cipher_text,shift_key):
	
	unshifted_cipher_text = ""	
	for orignal_chipher_char in original_cipher_text:
	
		shifted_char_index = ALPHABET.index(orignal_chipher_char)
		shift_key_index = ALPHABET.index(shift_key)
		
		if(shifted_char_index < shift_key_index):
			unshifted_char_index = shifted_char_index - shift_key_index + len(ALPHABET)
		else:
			unshifted_char_index = shifted_char_index - shift_key_index	
			
		unshifted_cipher_text += ALPHABET[unshifted_char_index]
		
	return unshifted_cipher_text
	
	
def b16_decode(encoded_string):
	decoded_string = ""
	for i in range(0,len(encoded_string),2):
		
		first_character = encoded_string[i]
		second_character = encoded_string[i+1]
	
		first_half_original = ALPHABET.index(first_character) << 4
		second_half_original = ALPHABET.index(second_character)
		
		full_original = first_half_original + second_half_original
		original_character = chr(full_original)
		
		decoded_string += original_character	
			
	return decoded_string
	



original_cipher_text = input("Enter cipher text : ")

for key in ALPHABET:

	unshifted_cipher_text = reverse_shift(original_cipher_text,key)
	
	flag = b16_decode(unshifted_cipher_text)
	
	print("\n Decoded string for key",key,":",flag)
