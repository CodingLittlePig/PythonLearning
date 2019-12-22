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
