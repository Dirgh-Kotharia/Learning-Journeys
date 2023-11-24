---
tags:
  - general-skills
points: 100 points
---

[<-- General Skills Write-ups](../writeup-list.md)

# strings it
## Write-up

##### Concept Coverage :
This challenge is introduction to a linux command line utility called [strings](https://www.howtogeek.com/427805/how-to-use-the-strings-command-on-linux/)

##### Following are the steps for the challenge: 
1. We are given a file with the challenge. At the time of writing the file was called `strings` but this might change.

2. We get a hint from the challenge title `strings it` and description mentioning `find the flag without running the file` that we need use a linux utility call `strings`. It is a simple utility that  print the strings of printable characters in files.

3. Upon using the `strings` command on the file (in my case, file was also called `strings`) we get a bunch of strings as output. So I used another utility called `grep` to see if we have a string in the output with `pico` in it and upon doing so I got the flag. we can submit the flag and complete the challenge.

    ```bash
    strings ./<file-name> | grep 'pico'
    ```

    ![flag](./assets/flag.png)