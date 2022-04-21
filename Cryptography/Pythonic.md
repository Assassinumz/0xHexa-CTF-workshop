# Challenge
Figure out the password from this python script

[main.py](./files/main.py)

# Solution
Open the python script in any text/code editor, we can notice that its printing the flag only if the `if` line at 7 is True so let's replace the condition there with `True`

Something like this:

```py
import string
strs = string.ascii_letters + string.digits + string.punctuation
pas = input("Enter the password: ")

pass_phrase = strs[15] + strs[24] + strs[59] + strs[7].upper() + strs[52] + strs[13].upper() + strs[87 + int(strs[53])]

if True:
    print(r"The password is the flag :P hexaCTF{" +  f"{pass_phrase + strs[28].lower().upper() + strs[54] + strs[50].lower() + strs[15].upper() + strs[45] + strs[52]}" + r"}")

else:
    print("Invalid password :(")
```
Now execute the script, provide any input and we will get the flag printed.

# Flag
	
hexaCTF{py7H0N_C2yPT0}