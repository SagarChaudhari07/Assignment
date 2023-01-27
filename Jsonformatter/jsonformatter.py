stack = []
top = 0
openingBrace = ['{','[']
closingBrace = ['}',']']

def push(char):
    global stack,top
    stack.append(char)
    top += 1

def pop():
    global stack,top
    stack = stack[:-1]
    top -= 1                                        

inputString = input()
outputString = ''

for char in inputString:
    #print("Stack is " ,stack, " top is ", top)
    if char in openingBrace:
        push(char)
        outputString += char+'\n'+'\t'*top
    elif char in closingBrace:
        pop()
        outputString += '\n'+'\t'*top+char
    elif char==',':
        outputString += char+'\n'+'\t'*top
    else:
        outputString += char

print("outputString:\n"+outputString)