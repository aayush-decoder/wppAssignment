def decode_msg(s, path="", res=[]):  
    if not s:  
        res.append(path)  
        return  

    if s[0] != '0':  
        decode_msg(s[1:], path + chr(int(s[0]) + 64), res)  

    if len(s) > 1 and '10' <= s[:2] <= '26':  
        decode_msg(s[2:], path + chr(int(s[:2]) + 64), res)  

    return res  

inp=input()  
ans= decode_msg(inp)  
print(ans)  
