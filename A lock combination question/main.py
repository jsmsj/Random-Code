from xmlrpc.server import list_public_methods


def mod(num:int):
    return num if num>=0 else -num

list_of_nums = [i for i in range(1,8)]
answer = [(x,y,z) for x in list_of_nums for y in list_of_nums for z in list_of_nums if x!=y and y!=z and x!=z and x>y and y>z and mod(x-y)>=2 and mod(y-z)>=2 and mod(x-z)>=2]
print(*answer,sep="\n")