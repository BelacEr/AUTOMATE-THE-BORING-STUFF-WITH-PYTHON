def list_str(value):
    output = ''
    for i in range(len(value)):
        if i != len(value) - 1: 
            output += str(value[i]) + ', '
        else:
            output += 'and ' + str(value[i])
    return output

list_value = ['apples', 'bananas', 'tofu', 'cats']
print(list_str(list_value))
