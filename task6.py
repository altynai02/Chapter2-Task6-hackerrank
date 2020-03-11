#Hackerrank balanced brackets

def isBalanced(s):
    dict_ = {'}': '{', ')': '(', ']': '['}
    list_ = []
    for i in s:
        if i in dict_.values():  
            list_.append(i)
        elif i in dict_.keys(): 
            if  list_ == [] or list_.pop() != dict_[i]:
                return "NO"
    if list_ == []:
        return "YES"
    else:
        return "NO"