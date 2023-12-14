---
tags:
  - general-skills
points: 100 points
---

[<-- General Skills Write-ups](../writeup-list.md)

# PW Crack 1
## Write-up

##### Concept Coverage :
This challenge covers basic python script knowledge.

##### Following are the steps for the challenge: 
1. We are given a python script and an encoded file containing the flag. At the time of writing the python script was named `level1.py` and encrypted flag file named `level1.flag.txt.enc` but this might change in future.

2. After downlaoding, I opened up the python script in an editor to read through the python file. we notice that we have open the `level1.flag.txt.enc` file and then it calls on the `level_1_pw_check()` function which takes `user_pw` as user input and then it validates if the input is equal to `8713`. if the validation succeeds it executes `str_xor()` function which seems to doing the decoding of the text from the `level1.flag.txt.enc`.

    - main function : 

      ![main](./assets/main.png)

    - str_xor function : 

      ![echoding-func](./assets/encoding-func.png)

3. I closed the editor and ran the script. Before running the script I ensured my `level1.flag.txt.enc` file is in same directory as `level1.py` python script. Upon running the script it asked for the password which we know is `8713` from reading the python script. As soon as we enter the password it gives us the flag.

    ![flag](./assets/falg.png)

4. We can submit the flag and complete the challenge
