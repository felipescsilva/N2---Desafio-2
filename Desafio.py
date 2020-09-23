#Felipe Soares - 081180008
#Compiladores - EC6 - 2020.2

#Entrada de dados por meio de digitacao no modo console.

def checkBalanced(value):
    s = []
    balanced = True
    index = 0

    if not checkValidate(value): return False

    while index < len(value) and balanced:

        value = value.replace(" ", "")
        char = value[index]
        if char in "<([{":
            s.append(char)
        else:
            if not s:
                balanced = False
            else:
                close = s.pop()
                if pares(close,char):
                       balanced = True
        index = index + 1
        
    if balanced and not s and len(value)!=0:
        return True
    else:
        return False

def pares(open,close):
    opens = "<([{"
    closers = ")]}>"
    return opens.index(open) == closers.index(close)

def checkValidate(value):
    access = ['(', ')', '{', '}', '[', ']', '<', '>', ' ']
    value = value.replace(" ", "")
    
    if len(value)==0: return False

    for i in range(0, len(value)):
        if value[i] not in access:
            return False
    return True


#Usado para testes diretos no codigo
#print(checkBalanced('{{([][])}()}'))

while True:
    print("Digite a sequencia desajada ou 0 para sair: ")
    entry = input()

    if entry=="0":
        break
    print(checkBalanced(entry))
