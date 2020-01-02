magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
magicians.append("hello")
print(magicians)
del magicians[2]
print(magicians)
print('\n2.统计有多少个用户')
print(len(magicians))
magicians.insert(0, "world")
print(magicians)
magicians.pop()
print(magicians)
magicians[0] = "hello hulk"
print(magicians)
magicians.pop(1)
print(magicians)
del magicians[1]
print(magicians)