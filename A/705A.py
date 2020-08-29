layer = int(input())
love = 'I love it'
hate = 'I hate it'
expression = ''
x = 0
while (layer - x - 1) > 0:
    if (layer - x) % 2 == 0:
        expression = 'I hate that ' + expression
    else:
        expression = 'I love that ' + expression
    x = x + 1
if layer % 2 == 0:
    print(expression + love)
else:
    print(expression + hate)
