# a = 1
# b = 2
# print(a, b)
# a, b = b, a
# print(a, b)

q = 7
w = 8
e = 9
r = 6
q, w, e, r = e, r, w, q
print(q, w, e, r)

print(type(q))
print(id(q))
print(id(e))