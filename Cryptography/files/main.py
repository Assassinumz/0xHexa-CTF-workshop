import string
strs = string.ascii_letters + string.digits + string.punctuation
pas = input("Enter the password: ")

pass_phrase = strs[15] + strs[24] + strs[59] + strs[7].upper() + strs[52] + strs[13].upper() + strs[87 + int(strs[53])]

if pas == pass_phrase + strs[28].lower().upper() + strs[54] + strs[50].lower() + strs[15].upper() + strs[45] + strs[52]:
    print(r"The password is the flag :P hexaCTF{" +  f"{pass_phrase + strs[28].lower().upper() + strs[54] + strs[50].lower() + strs[15].upper() + strs[45] + strs[52]}" + r"}")

else:
    print("Invalid password :(")