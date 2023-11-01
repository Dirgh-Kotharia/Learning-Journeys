---
tags:
  - reverse-engineering
points: 30 points
---

[<-- PicoCTF Category Table](../../README.md#2-picoctf)

# crackme-py

## Write-up
##### Concept Coverage :
This challenge is pretty straight forward and covers the concept of the hidden code

##### Following are the steps for the challenge: 
1. Download the python script given with the challenge. upon reading through the python script a few things standout.
2. Firstly, we have variable that might contain our flag but it seems to be encoded.
    
    ![encoded-variable](../assets/crackme-py/encoded-variable.png)
    
3. Secondly, we notice that there is a decode function which seems not to be invoked anywhere in the main function.
    
    ![decoding-function](../assets/crackme-py/decoding-function.png)
    
4. At last we have a main portion of the python script which run when we executed when we run it
    
    ![main-function](../assets/crackme-py/main-function.png)
    
5. As the decode function is never invoked, lets add a method to call `decode_secret` with `bezos_cc_secret` as a parameter so that the method is called we can leverage it to decode. Example : 
    
    ![updated-code](../assets/crackme-py/updated-code.png)
    
6. now upon executing the python script I get the flag : 
    
    ![flag-output](../assets/crackme-py/flag-output.png)

