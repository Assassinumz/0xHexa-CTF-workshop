# Challenge
They say its a ver BASEic encryption. `aGV4YUNURntiQFNpQ19FTmMyeVAxaU9ufQ==`

# Solution
We can figure out its a base64 encryption with the emphasize on BASE and the double = in the end. But just to be sure you can use any online cipher identifier to figure out the cipher.

https://www.dcode.fr/cipher-identifier After pasting the string in here it says it's a base64 encryption

Now to decrypt it use any base64 decoder https://www.base64decode.org/ after pasting the encrypted string here and decoding it we get the flag.

# Flag
hexaCTF{b@SiC_ENc2yP1iOn}