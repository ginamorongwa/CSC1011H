
num_frogs = int(input('Enter the number of frogs:\n'))
num_toads = int(input('Enter the number of toads:\n'))
state = ['Frog']*num_frogs+['']+['Toad']*num_toads
final_state = ['Toad']*num_toads+['']+['Frog']*num_frogs
for i in range(1, (num_toads+num_frogs+2)):
    print('   {}'.format(i), end='')
print("")
for j in range(0, (num_toads+num_frogs+1)):
    print('{}'.format(state[j]), end='')
    if state[j] == '':
        print("    ", end='')
print("")

while True:
    index = input(">")

    if index == "quit":
        break
    else:
        index = int(index)
        if state[index-1] == 'Frog':
            if state[index] == '':
                state[index] = 'Frog'
                state[index-1] = ''
            elif (state[index] == 'Frog' or state[index] == 'Toad') and state[index+1] == '':
                state[index+1] = 'Frog'
                state[index-1] = ''
        else:
            if state[index-1] == 'Toad':
                if state[index-2] == '':
                    state[index-2] = 'Toad'
                    state[index-1] = ''
                elif (state[index-2] == 'Frog' or state[index-2] == 'Toad') and state[index-3] == '':
                    state[index-3] = 'Toad'
                    state[index-1] = ''

        # print state
        for i in range(1, (num_toads+num_frogs+2)):
            print('   {}'.format(i), end='')
        print("")
        for j in range(0, (num_toads+num_frogs+1)):
            print('{}'.format(state[j]), end='')
            if state[j] == '':
                print("    ", end='')
        print("")

        if state == final_state:
            print("Congratulations, you've won!")
            break

        #TODO: check if any more moves can be made