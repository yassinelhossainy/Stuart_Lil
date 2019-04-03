from random import randint
import random
import time
import os
import operator
numberchoosing = 0




def greetings():
    name = input('Hello I am Python Random Equation Creator! [PREC for short!] what is your name? ').title()
        
    print ('''Hello {}, it is wonderful to meet you! Here is a quick tutorial of how PREC works!
            Just a couple of notes, the program assists you along the way!
            You can use powers, squares and cube numbers [ex. 9**2 = nine to the power of 2/time squared].
            The division sign is the backslash, it is converted to the standard division sign [÷]
            When typing in the file, the file doesn't need to exit. If it already does exit the file will be updated with new equations
            A session of using PREC generates 2 files, a question sheet and an answer sheet [Which is the name of the question sheet with _Answers added to it.]
            Be careful when typing in an answer if you mess up you will have to restart [don't worry its a short process]
            You can press the 'Enter' key instead of 'n' to say no.
            Have fun!

            
            
            [PREC Was Made By Yassin Elhossainy]'''.format(name))
        

    delete = input('Do you want to delete a file?[y/n].This is optional, you can delete basically any folder, but you can use it to delete a previous folder that you made in PREC').lower()
    if delete == 'y':
                
                deletew = input('Enter the filename you want to delete[Remember you have to be exact and precise] ')
                os.remove('{}.txt'.format(deletew))
                
                print ('File deleted!')
    else:
                
                print ('Ok lets continue with your test!')

    return (name)


def intro():
    

    
    
    filename = input('Enter a file name for your quiz! ')
    title = input('Do you want to add a title to your test? [y/n] ').lower()
    if title == 'y':
            titlename = input('Alright! What do you want to name your title? ')
            Quiz = open(f'{filename}.txt', 'a')
            Quiz.write(titlename + '\n')
            Quiz.close()
    else:
            print ('Alright lets cotinue with your quiz!')


        
    
    namew = input('Do you want add a section were test-takers write their name? [y/n] ').lower()
    if namew == 'y':
            Quiz = open(f'{filename}.txt', 'a')
            Quiz.write('Name:_________________' + '\n')
            Quiz.close()
    else:
           print ('Alright lets continue with your quiz!')

    schoolname = input('Do you want add a section were test-takers write the name of their school [y/n] ').lower()
    if schoolname == 'y':
            Quiz = open(f'{filename}.txt', 'a')
            Quiz.write('School Name:_________________' + '\n')
            Quiz.close()
    else:
           print ('Alright lets continue with your quiz!')


        
    date = input('Do you want to add a section where test-takers write down the date? [y/n] ').lower()
    if date == 'y':
            datetype = input('How do you want to do it? A [Date:____/____/____] or B [Date:__________________________]? [A/B] ').lower()
            if datetype == 'a':
                    print ('Alright!')
                    Quiz = open(f'{filename}.txt', 'a')
                    Quiz.write('Date:____/____/____' + '\n')
                    Quiz.close()
            elif datetype == 'b':
                    Quiz = open(f'{filename}.txt', 'a')
                    Quiz.write('Date:__________________________' + '\n')
                    Quiz.close()

    rownding = input('Do you want add a section where it says how many decimal decimal points to round up too?[y/n] ').lower()
    if schoolname == 'y':
            rownding_number = input('Alright type in how many decimal points you want to round up to [use numbers] ')
            print ('Alright!')
            Quiz = open(f'{filename}.txt', 'a')
            Quiz.write(f'Round up to: {rownding_number} decimal points' + '\n')
            Quiz.close()
    else:
           print ('Alright lets continue with your quiz!')
           
    global questions
    questions = int(input('How many questions do you want? '))



    
    return (numberchoosing, filename)

    
   
    

def numbersint(numberchoosing, filename):
    numberchoosing += 1
    equations = 0
    operationtype = ''
    while questions == equations:              
        print ('Thank you for using PREC!, You have created a question file and and answer file!')
        break
    while questions != equations:    
        while numberchoosing == 1: 
            first_num_minimum = int(input('Enter the minimum amount for your first operant '))
            
            first_num_maximum = int(input('Enter the maximum amount for your first operant '))
            
           
            if first_num_maximum < first_num_minimum:
                
                print ('Sorry, your minimum value is larger than your maximum value!, please start again!')
                break
            
            second_num_minimum = int(input('Enter the minimum amount for your second operant '))
           
            second_num_maximum = int(input('Enter the maximum amount for your second operant  '))
            
            if second_num_maximum < second_num_minimum:
                
                print ('Sorry, your minimum value is larger than your maximum value!, please start again!')
                break

           
            

           
            operation = input('Enter the operator [+, -, x, /]')
            if operation == '/':
                operation = '÷'
                operationtype = f'Division Questions [{operation}]:'
                Quiz = open(f'{filename}.txt', 'a')
                Quiz.write(operationtype  + '\n' + '\n' )
                Quiz.close()
                numberchoosing += -1
                
               
            elif operation == 'x':
                operationtype = f'Multiplication Questions [{operation}]:'
                Quiz = open(f'{filename}.txt', 'a')
                Quiz.write(operationtype  + '\n' + '\n')
                Quiz.close()
                numberchoosing += -1
                
           
            elif operation == '+':
                operationtype = f'Additon Questions [{operation}]:'
                Quiz = open(f'{filename}.txt', 'a')
                Quiz.write(operationtype  + '\n' + '\n' )
                Quiz.close()
                numberchoosing += -1
                
             
            elif operation == '-':
                operationtype = f'Subtraction Questions [{operation}]:'  
                Quiz = open(f'{filename}.txt', 'a')
                Quiz.write(operationtype  + '\n' + '\n' )
                Quiz.close()
                numberchoosing += -1
            
          
            else:
                print ('Oops! It looks like you put in an incorrect value! Please restart PREC.')
                break
            return (filename, first_num_minimum, first_num_maximum,  second_num_minimum, second_num_maximum, operation,equations)



def numbersflt(numberchoosing, filename):
    numberchoosing += 1
    equations = 0
    operationtype = ''
  
    while questions != equations:    
        while numberchoosing == 1: 
            first_num_minimum = float(input('Enter the minimum amount for your first operant '))
            
            first_num_maximum = float(input('Enter the maximum amount for your first operant '))
            
           
            if first_num_maximum < first_num_minimum:
                
                print ('Sorry, your minimum value is larger than your maximum value!, please start again!')
                break
            
            second_num_minimum = float(input('Enter the minimum amount for your second operant '))
           
            second_num_maximum = float(input('Enter the maximum amount for your second operant  '))
            
            if second_num_maximum < second_num_minimum:
                
                print ('Sorry, your minimum value is larger than your maximum value!, please start again!')
                break

           
            

           
            operation = input('Enter the operator [+, -, x, /]')
            if operation == '/':
                operation = '÷'
                operationtype = f'Division Questions [{operation}]:'
                Quiz = open(f'{filename}.txt', 'a')
                Quiz.write(operationtype  + '\n' + '\n' )
                Quiz.close()
                numberchoosing += -1
                
               
            elif operation == 'x':
                operationtype = f'Multiplication Questions [{operation}]:'
                Quiz = open(f'{filename}.txt', 'a')
                Quiz.write(operationtype  + '\n' + '\n')
                Quiz.close()
                numberchoosing += -1
                
           
            elif operation == '+':
                operationtype = f'Additon Questions [{operation}]:'
                Quiz = open(f'{filename}.txt', 'a')
                Quiz.write(operationtype  + '\n' + '\n' )
                Quiz.close()
                numberchoosing += -1
                
             
            elif operation == '-':
                operationtype = f'Subtraction Questions [{operation}]:'  
                Quiz = open(f'{filename}.txt', 'a')
                Quiz.write(operationtype  + '\n' + '\n' )
                Quiz.close()
                numberchoosing += -1
            
          
            else:
                print ('Oops! It looks like you put in an incorrect value! Please restart PREC.')
                break
            return (filename, first_num_minimum, first_num_maximum,  second_num_minimum, second_num_maximum, operation,equations)



            
def writeflt(filename, first_num_minimum, first_num_maximum,  second_num_minimum, second_num_maximum, operation,equations):
        
                     
            while questions != equations:
                    firstnum = random.uniform(first_num_minimum, first_num_maximum)
                    secondnum = random.uniform(second_num_minimum, second_num_maximum)
                    round (firstnum, 1)
                    round (secondnum, 1)
                            
                    
                                
                               
                    if operation == 'x': 
                                    answers = firstnum * secondnum
                    elif operation == '+':
                                    answers = firstnum + secondnum
                    elif operation == '-':
                                    answers = firstnum - secondnum
                    elif operation == '÷':
                                    answers = firstnum / secondnum

                                    
                    firstnumstr = str(firstnum)
                    secondnumstr = str(secondnum)
                    equations += 1  
                    equation = '{}: {} {} {} = '.format(equations, firstnumstr, operation , secondnumstr)
                    answer = ('''This is the answer to this equation [{}]
                                {}'''.format(equation,answers))
                                
                     
                    print (equation + 'This is your #{} equation'.format(equations))
                    print (answer)

                                  
                    Quiz = open(f'{filename}.txt', 'a')
                    Quiz.write(equation  + '\n' + '\n')
                    Quiz.close()
                    time.sleep(0.1)

                    Quiz = open(f'{filename}_Answers.txt', 'a')
                    Quiz.write(equation + ':' + '\n' + answer +'\n')
                    Quiz.close()
                    time.sleep(0.1)
            return (filename, firstnum, secondnum)



def writeint(filename, first_num_minimum, first_num_maximum,  second_num_minimum, second_num_maximum, operation,equations):
    
                     
            while questions != equations:
                
                   
                    firstnum = randint(first_num_minimum ,first_num_maximum)
                    secondnum = randint(second_num_minimum , second_num_maximum)
                            
                    if operation == 'x': 
                        answers = firstnum * secondnum
                    elif operation == '+':
                                    answers = firstnum + secondnum
                    elif operation == '-':
                                    answers = firstnum - secondnum
                    elif operation == '÷':
                                    answers = firstnum / secondnum
                                       
                    firstnumstr = str(firstnum)
                    secondnumstr = str(secondnum)
                    equations += 1
                    equation = '{}: {} {} {} = '.format(equations, firstnumstr, operation , secondnumstr)
                    answer = ('''This is the answer to this equation [{}]
                                {}'''.format(equation,answers))
                                
                    
                    print (equation + 'This is your #{} equation'.format(equations))
                    print (answer)

                                  
                    Quiz = open(f'{filename}.txt', 'a')
                    Quiz.write(equation  + '\n' + '\n')
                    Quiz.close()
                    time.sleep(0.1)

                    Quiz = open(f'{filename}_Answers.txt', 'a')
                    Quiz.write(answer +'\n' + '\n')
                    Quiz.close()
                    time.sleep(0.1)
            return (filename)


def end(filename):
    whattodo = input(f'''Your {filename} and an answer sheet has been created/updated! What do you want to do now?
A:Start over
B:Exit PREC ''').lower()
    if whattodo == 'b':
        print ('Thank you for using prec!, I hope you will use it again in the near future!')
        mainintrpt()

    elif whattodo == 'a':
        print ('Alright, restarting PREC')
        starter()
    else:
        print ('Thank you for using prec! Hopefully you will use it again! Goodbye!')

        
    return (filename)

###########
def mainintrpt():
    filename = input('Enter the filename that you want to update ')
    questions = int(input('How many questions do you want?'))
    filename, first_num_minimum, first_num_maximumm,  second_num_minimum, second_num_maximumm, operation,equations  =  numbersflt(numberchoosing, filename)
    filename = writeflt(filename, first_num_minimum, first_num_maximumm,  second_num_minimum, second_num_maximumm, operation,equations )
    filname = end(filename)

def mainfltrpt():
    filename = input('Enter the filename that you want to update ')
    questions = int(input('How many questions do you want?'))
    filename, first_num_minimum, first_num_maximumm,  second_num_minimum, second_num_maximumm, operation,equations  =  numbersflt(numberchoosing, filename)
    filename = writeflt(filename, first_num_minimum, first_num_maximumm,  second_num_minimum, second_num_maximumm, operation,equations )
    filname = end(filename)

    
    
    

def numbertype():
    numberr = input('Do you want to use floats [decimal numbers] or integers [normal numbers]? [f/i] ')
    if numberr == 'f':
        print ('You will be using float [decimal] numbers]')
        mainflt()
    else:
        print ('You will be using integers [normal] numbers')
        mainint()


def mainint():
    numberchoosing, filename = intro()
    filename, first_num_minimum, first_num_maximum,  second_num_minimum, second_num_maximum, operation, equations  =  numbersint(numberchoosing, filename)
    filename = writeint(filename, first_num_minimum, first_num_maximum,  second_num_minimum, second_num_maximum, operation,equations )
    filename = end(filename)
        

def mainflt():
    numberchoosing, filename = intro()
    filename, first_num_minimum, first_num_maximum,  second_num_minimum, second_num_maximum, operation,equations  =  numbersflt(numberchoosing, filename)

    filename = writeflt(filename, first_num_minimum, first_num_maximum,  second_num_minimum, second_num_maximum, operation,equations )
    filname = end(filename)

def starter():
    greetings()
    numbertype()

starter()
