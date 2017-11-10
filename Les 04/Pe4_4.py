def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >=6 :
        for c in newpassword:
            if c in '0123456789' :
                return True
        return False
    else :
        return False

res = new_password('vakProgmm', 'Python17')
print(res)

print(new_password('huProg17', 'huProg17'))

print(new_password('vakProg17', 'Pro17'))

print(new_password('vakProg17', 'jammerjoh'))