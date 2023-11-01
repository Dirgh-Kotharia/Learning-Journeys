---
tags:
  - forensics
points: 10 points
---

[<-- Forensics Write-ups](../writeup-list.md)

# Information

## Write-up
##### Concept Coverage :
This is an introductory Challenge to forensics. this helps us explore the concepts of metadata of a file

##### Following are the steps for the challenge: 
1. Download the image file from the challenge.
2. Upon opening file and inspecting, nothing seems to standout in terms of flag.
3. As a next step we try to explore the metadata for potential clues. For this you can utilize a linux utility called [exiftool](https://en.wikipedia.org/wiki/ExifTool) or you can use online metadata extractors like [this one](https://exif.tools/) .
   
```bash
exiftool <image-file-name>
```
  
4. The license field stands out as it has an base 64 encoded value rather than an URL / name of the license. we can try to decrypt that value using linux utility of [base64](https://www.geeksforgeeks.org/convert-text-file-strings-into-base64-encoding/) or an online decoder like [this one](https://www.base64decode.org/). Upon decrypting we get our flag.
   
```bash
echo "<base64-encoded-text>" | base64 -d
```