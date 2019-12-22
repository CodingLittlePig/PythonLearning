bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
print(bicycles[-1].title())
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)
bicycles[0] = 'honda'
print(bicycles)

bicycles.append('ducati')
print(bicycles)

bicycles.insert(0, 'ducati')
print(bicycles)

del bicycles[0]
print(bicycles)

print(bicycles.pop())
print(bicycles)
bicycles.pop(0)
print(bicycles)
bicycles.remove('redline')
print(bicycles)

bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)
bicycles.reverse()
print(bicycles)

print(len(bicycles))