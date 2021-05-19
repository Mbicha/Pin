#Default Pin
pin = 1234

#Counter
pin_counter = 0

for pin_counter in range(3):
    #user Input Prompt
    enter_pin = int(input('Enter Your Pin'))
    if enter_pin == pin:
        print('Pin Correct')
        exit()
    else:
        print('Pin Incorrect')
        pin_counter +=1
else:
    print('Blocked')
    exit()
