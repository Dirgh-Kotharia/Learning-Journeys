---
tags:
  - reverse-engineering
points: 30 points
---

[<-- Reverse Engineering Skills Write-ups](../writeup-list.md)

# Keygenme-py

## Write-up
##### Concept Coverage :
This challenge covers the basic understanding of python. The flag is present in the code as key is the license to unlock the full version of given python program 

##### Following are the steps for the challenge: 
1. Download the python script provided with the challenge.
2. Upon opening and going through the file we notice things. Firstly, we notice that we are given full flag except for 1 part.
    
    ![hidden-flag](./assets/hidden-flag.png)
    
3. Secondly we notice that there is a `check_key()` function which checks the entered key against the actual key to figure out whether the entered key is valid of not. there are a few things to notice in the `check_key()` function :
    
     1. Initially , there is a loop which checks the entered key with first `key_part_static_trial` character by character so we know that first part of the flag is value of `key_part_static_trial` .
        
        ![key-check-1](./assets/key-check-1.png)
        
     2. For second part of the key . they take the value of variable `username_trial` and hashes it to SHA256 and picks the character in jumbled order. . we can easily replicate the process to find what out put it generates
        
        ![key-check-2](./assets/key-check-2.png)
    3. Then we can complete the key by attaching the last part `key_part_static2_trial` which is just `}` .
4. Now that we have a theory in mind lets write a basic code the generate the key. You can try to write your own code from the understanding above or if you want the code you can use this one :  [generate-key.py](./assets/generate-key.py). Running the program prints the flag.
   
    ![full-flag](./assets/full-flag.png)  
