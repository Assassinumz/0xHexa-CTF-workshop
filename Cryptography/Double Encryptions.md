# Challenge
Can you decrypt this to get the flag? `LS4uIC0tLS0tIC4uLSAtLi4uIC4tLi4gLiAuIC0uIC0uLS4gLi0uIC0uLS0gLi0tLiAtIC0uLS4tLSAtLS0gLS4=`

Enclose the flag in: hexaCTF{}

# Solution
The encrypted string ends with `=` so its again a base64 cipher after using any base64 decoder https://www.base64decode.org/ we get: `-.. ----- ..- -... .-.. . . -. -.-. .-. -.-- .--. - -.-.-- --- -.`

Let's use online cipher identifier for this https://www.dcode.fr/cipher-identifier and we figure out its an morse code.

Using any morse code decoder we get the flag
`D0UBLEENCRYPT!ON` enclose it in `hexaCTF{}`

# Flag
hexaCTF{D0UBLEENCRYPT!ON}
