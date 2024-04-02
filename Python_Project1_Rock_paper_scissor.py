import random

Choices = ['Rock', 'Paper', 'Scissor']
User_Choice = input('Enter your choice :')
Random_computer_choice = random.choice(Choices)
print ('Computer Choice: ', Random_computer_choice)


while True:
 
    if User_Choice == Random_computer_choice:
       print('It is a tie.')

    elif User_Choice == 'Rock' and Random_computer_choice == 'Scissor':
        print ('Rock wins against scissor. \n You WON and Computer Lost.')

    elif User_Choice == 'Paper' and Random_computer_choice == 'Rock':
        print ('Paper wins against scissor. \n You WON and Computer Lost')

    elif User_Choice == 'Scissor' and Random_computer_choice == 'Paper':
        print('Scissor wins againt paper. \n You WON and Computer Lost')

    else:
        print ('Computer WON! \n You Lost!')

    New_operation = input('Do you want to proceed with another operation(yes/no):')

    if New_operation == 'no':
      break

    if New_operation == 'yes':
        User_Choice = input('Enter your choice :')
        Random_computer_choice = random.choice(Choices)
        print ('Computer Choice: ', Random_computer_choice)
        





   


