## Please note the values here are from my challenge they can change so please check and ensure proper values are in place

import hashlib

username_trial = b"FREEMAN" ## value from the challenge provided code used in check_key() function

## we know first part of the full key is value of'key_part_static1_trial' variable from the code provided in challenge
key_part_1 = "picoCTF{1n_7h3_|<3y_of_"

## The second part of the key we will have to derive
key_part_2 = ""

## We also know the last part of the key is value of'key_part_static2_trial' variable from the code provided in challenge
key_part_3 = "}"

jumbled_order = [4,5,3,6,2,7,1,8]  ## order in which hash values are compared

hash_value = hashlib.sha256(username_trial).hexdigest() ## hash_value 

## now to generate the hidden part of flag
hidden_values = []
for i in jumbled_order:
    hidden_values.append(hash_value[i])

key_part_2 = "".join(hidden_values)

full_key = key_part_1 + key_part_2 + key_part_3 ## The full key - also our flag

print(full_key)


