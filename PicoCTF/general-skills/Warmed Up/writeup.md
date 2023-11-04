---
tags:
  - general-skills
points: 50 points
---

[<-- General Skills Write-ups](../writeup-list.md)

# Warmed Up
## Write-up

##### Concept Coverage :
This was a introduction to convert hex to Decimal

##### Following are the steps for the challenge: 
1. We are asked what would hex value `0x3d` represent in decimal
   
2. We can use the below bash code to get the output. 
   
```bash
echo $((16#3d))
```

```bash
python -c 'print(int("3d", 16))'
```

3. You can also use online tool like [rapidtables](https://www.rapidtables.com/convert/number/hex-to-decimal.html) for quick solve 
    
    ![rapid-tables](./assets/rapid-tables.png)

4. You can replace `3d` with a different hex value as asked by your challenge and you just need to wrap the response with `picoCTF{}` and submit the flag.