expr = str(input('Digite uma expressão: '))
pilha = []

for char in expr:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.apend((')'))
            break

if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')
