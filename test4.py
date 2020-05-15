f = 'john'
la = 'smith'
message = f + ' [' + la + '] is a coder.'
msg = f'{f} [{la}] is a coder.'
print(message, len(message), msg, len(msg))
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.find('h')+1)
print(msg.replace('smith', 'sins'))
print('john' in msg)
