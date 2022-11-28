s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

# lst = s.split()
# result = {}
# for elem in lst:
#     key, val = elem.split(':')
#     result[int(key)] = val

# result = {int(elem.split(':')[0]): elem.split(':')[1] for elem in s.split()}
result = {int(key):val for key, val in [elem.split(':') for elem in s.split()]}
print(result)


