---
tags:
  - cryptography
points: 10 points
---
## Write-up
##### Concept Coverage :
This challenge is an introduction to cryptography. It covers one of the simpler algorithms called [ROT13](https://en.wikipedia.org/wiki/ROT13) . 

##### Following are the steps for the challenge: 
1. Copy the text from challenge. The text is encoded using ROT13 encryption. it is reversible by a simple decoding
2. You can utilize an online ROT13 decoder like this one from [cryptii](https://cryptii.com/pipes/rot13-decoder) or you can use the [**"tr"**](https://www.geeksforgeeks.org/tr-command-in-unix-linux-with-examples/) command in the terminal to do it
```bash
echo "<replace-text-here>" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
3. The output should give the flag
