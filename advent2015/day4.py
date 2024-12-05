import hashlib
 
# encoding GeeksforGeeks using md5 hash
# function 
str2hash = "iwrupvqb"
result = ""
ans =  0
while result == "" or not result.hexdigest().startswith("000000"):
    whole = str2hash + str(ans)
    result = hashlib.md5(whole.encode())
    ans+=1

print(ans-1)

