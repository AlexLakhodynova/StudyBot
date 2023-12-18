import telebot  
import time  
import requests   

token = '6757963944:AAGly8I3FzkIdqSBgMtKQWSgWe24pq2rCQs'   


kase = telebot.types.ReplyKeyboardMarkup(True,False)
kase.row('Flowcharts','Operators' )
kase.row('Data types','Searching algorithms')
bot = telebot.TeleBot(token)

answers1 = telebot.types.ReplyKeyboardMarkup(True,False)
answers1.row('Yes','No')

TypesAnswers = telebot.types.ReplyKeyboardMarkup(True,False)
TypesAnswers.row('Integer','Real' )
TypesAnswers.row('Boolean','Character', "String")

OperatorsAnswers = telebot.types.ReplyKeyboardMarkup(True,False)
OperatorsAnswers.row('+','/','-','^')
OperatorsAnswers.row('MOD','*','DIV')


confirmation = telebot.types.ReplyKeyboardMarkup(True,False)
confirmation.row('Ok')

FlowchartsAnswers = telebot.types.ReplyKeyboardMarkup(True,False)
FlowchartsAnswers.row('oval','parallelogram','rhombus','line', "rectangle")

BubbleAnswers = telebot.types.ReplyKeyboardMarkup(True,False)
BubbleAnswers.row('1','16','8','9')
BubbleAnswers.row('4','5','2', '6')

numAnswers = telebot.types.ReplyKeyboardMarkup(True,False)
numAnswers.row('5,1','4,6','3,2')
numAnswers.row('5,3','4,2')

passAnswers = telebot.types.ReplyKeyboardMarkup(True,False)
passAnswers.row('1,5,2,3,4,6')
passAnswers.row('1,3,2,4,5,6')

mergeAnswers = telebot.types.ReplyKeyboardMarkup(True,False)
mergeAnswers.row('single items','pairs')
mergeAnswers.row('whole list','groups')

def pars(text , html_text):
    a = html_text.find(text) 
    b = html_text[a:a+100]
    b = b.replace('</td>' , '\n') 
    bb = b.rfind('<td>')
    br = b.rfind('</tr') 
    return (b[bb+4:br])


bot.state = 'Init'
bot.Sub_state = 'Init'
bot.incorrect = []
bot.results = 0
bot.wrong = 0

bot.Topic2State = 'Init'
bot.Topic3State = 'Init'
bot.Topic4State = 'Init'

                                                                                                       

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, "Hello, I'm your assistant, here you can revise for your exam. Are you ready for revision?", reply_markup=answers1)

def permition(message):
    if message.text.lower() == 'yes':
        bot.send_message(message.chat.id, "Then, let's start")
        bot.send_message(message.chat.id, "At the bottom, you can choose topic for revision ", reply_markup=kase)
        bot.state = 'Start'
    elif message.text.lower() == 'no':
        bot.send_message(message.chat.id, "Okey, maybe next time", reply_markup=answers1)



def ChooseTopic(message):
    if 'Flowcharts' in message.text:
        bot.state = 'Flowcharts'

    elif 'Operators' in message.text:
        bot.state = 'Operators'

    elif 'Data types' in message.text:
        bot.state = 'Data types'

    elif 'Searching algorithms' in message.text:
        bot.state = 'Searching algorithms'

def FlowchartsQuestion1(message):
    bot.send_message(message.chat.id, "What is the shape of the terminal?",reply_markup=FlowchartsAnswers)
    bot.Sub_state = 'Q1'
def FlowchartsQuestion2(message):
    bot.send_message(message.chat.id, "What is the shape of the input/output?",reply_markup=FlowchartsAnswers)
    bot.Sub_state = 'Q2'
def FlowchartsQuestion3(message):
    bot.send_message(message.chat.id, "What is the shape of the decision?",reply_markup=FlowchartsAnswers)
    bot.Sub_state = 'Q3'
def FlowchartsQuestion4(message):
    bot.send_message(message.chat.id, "What is shows direction of flow?",reply_markup=FlowchartsAnswers)
    bot.Sub_state = 'Q4'
def FlowchartsQuestion5(message):
    bot.send_message(message.chat.id, "What is the shape of the process?",reply_markup=FlowchartsAnswers)
    bot.Sub_state = 'Q5'
    
def FlowchartsAnswer1(message):
    if message.text.lower() == 'oval':
        bot.results += 1   
        bot.send_message(message.chat.id, f"Well done, that is right. 4 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is oval try to do other 4",)
        bot.wrong += 1
    

def FlowchartsAnswer2(message):
    if message.text.lower() == 'parallelogram':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 3 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is parallelogram try to do other 3",)
        bot.wrong += 1
     

def FlowchartsAnswer3(message):
    if message.text.lower() == 'rhombus':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 2 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is rhombus try to do other 2",)
        bot.wrong += 1
     
    
def FlowchartsAnswer4(message):
    if message.text.lower() == 'line':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 1 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is line try to do other 1",)
        bot.wrong += 1 
     
    
def FlowchartsAnswer5(message):
    if message.text.lower() == 'rectangle':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 0 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is rectangle",)
        bot.wrong += 1
    bot.send_message(message.chat.id, f"In the questions about flowcharts you answered correctly {bot.results} time and incorrectly {bot.wrong} times", )
    bot.send_message(message.chat.id, "Also remember that: ALGORITHMS - is a process or set of rules to be followed in calculations or other problem-solving operations, especially by a camputer",)
    bot.send_message(message.chat.id, "DECOMPOSITION - involves breaking down a large problem into smaller sub-problems",)
    bot.send_message(message.chat.id, "ABSTRACTION - involves removing unnecessary detail from aproblem, so that you can focus on the essential components",) 
    bot.send_message(message.chat.id, "SEQUENCE - a series  of steps which are complete one after the other",)
    bot.send_message(message.chat.id, "SELECTION - the ability to choose different paths throough a program",)
    bot.send_message(message.chat.id, "ITERATION - repeating a part of a program",) 
    bot.Sub_state = 'Init'
    bot.state = 'Init'
    bot.results = 0
    bot.wrong = 0


def OperatorsQuestion1(message):
    bot.send_message(message.chat.id, "What is the symbol for Addition?",reply_markup=OperatorsAnswers)
    bot.Sub_state = 'Q1'
def OperatorsQuestion2(message):
    bot.send_message(message.chat.id, "What is the symbol for Subtraction?",reply_markup=OperatorsAnswers)
    bot.Sub_state = 'Q2'
def OperatorsQuestion3(message):
    bot.send_message(message.chat.id, "What is the symbol for Division?",reply_markup=OperatorsAnswers)
    bot.Sub_state = 'Q3'
def OperatorsQuestion4(message):
    bot.send_message(message.chat.id, "What is the symbol for Multiplication?",reply_markup=OperatorsAnswers)
    bot.Sub_state = 'Q4'
def OperatorsQuestion5(message):
    bot.send_message(message.chat.id, "What is the symbol for Exponent?",reply_markup=OperatorsAnswers)
    bot.Sub_state = 'Q5'
def OperatorsQuestion6(message):
    bot.send_message(message.chat.id, "What is the symbol for Modulo(remainder)?",reply_markup=OperatorsAnswers)
    bot.Sub_state = 'Q6'
def OperatorsQuestion6(message):
    bot.send_message(message.chat.id, "What is the symbol for Integer division?",reply_markup=OperatorsAnswers)
    bot.Sub_state = 'Q7'
    
def OperatorsAnswer1(message):
    if message.text.lower() == '+':
        bot.results += 1   
        bot.send_message(message.chat.id, f"Well done, that is right. 5 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is + oval try to do other 5",)
        bot.wrong += 1
    

def OperatorsAnswer2(message):
    if message.text.lower() == '-':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 4 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is - try to do other 4",)
        bot.wrong += 1
     

def OperatorsAnswer3(message):
    if message.text.lower() == '/':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 3 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is / try to do other 3",)
        bot.wrong += 1
     
    
def OperatorsAnswer4(message):
    if message.text.lower() == '*':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 2 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is * try to do other 2",)
        bot.wrong += 1 
     
def OperatorsAnswer5(message):
    if message.text.lower() == '^':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 1 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is ^ try to do other 1",)
        bot.wrong += 1 

def OperatorsAnswer6(message):
    if message.text.lower() == 'MOD':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 1 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is MOD try to do other 1",)
        bot.wrong += 1 
          
    
def OperatorsAnswer7(message):
    if message.text.lower() == 'DIV':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 0 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is DIV",)
        bot.wrong += 1
    bot.send_message(message.chat.id, f"In the questions about foperators you answered correctly{bot.results} time and incorrectly{bot.wrong} times", )
    bot.send_message(message.chat.id, "Also remember that: LESS THEN - <",)
    bot.send_message(message.chat.id, "LESS THEN or EQUAL TO - ≤",)
    bot.send_message(message.chat.id, "GREATER THEN - >",)
    bot.send_message(message.chat.id, "GREATER THEN or EQUAL TO - ≥",)
    bot.send_message(message.chat.id, "EQUAL TO - =",)
    bot.send_message(message.chat.id, "NOT EQUAL TO - ≠",)
    bot.send_message(message.chat.id, "ASSIGMENTS - ←  ",)
    bot.send_message(message.chat.id, "BRANCH DEPENDING ON CONDITION  - IF/ELSE",)
    bot.send_message(message.chat.id, "GET USER INPUT - INPUT",)
    bot.send_message(message.chat.id, "OUTPUT TO THE USER - OUTPUT",)
    bot.send_message(message.chat.id, "REPEAT A SET OF NUMBER OF TIME - FOR",)
    bot.send_message(message.chat.id, "REPEAT WHILE A CONDITION IS TRUE - WHILE ",)
    bot.Sub_state = 'Init'
    bot.state = 'Init'
    bot.results = 0
    bot.wrong = 0

def Data_TypesQuestion1(message):
    bot.send_message(message.chat.id, "What is a whole number?",reply_markup=TypesAnswers)
    bot.Sub_state = 'Q1'
def Data_TypesQuestion2(message):
    bot.send_message(message.chat.id, "What is a number with a decimal point?",reply_markup=TypesAnswers)
    bot.Sub_state = 'Q2'
def Data_TypesQuestion3(message):
    bot.send_message(message.chat.id, "What can only be True or False ?",reply_markup=TypesAnswers)
    bot.Sub_state = 'Q3'
def Data_TypesQuestion4(message):
    bot.send_message(message.chat.id, "What is a single alphabetic or numeric character?",reply_markup=TypesAnswers)
    bot.Sub_state = 'Q4'
def Data_TypesQuestion5(message):
    bot.send_message(message.chat.id, "What is one or more characters enclosed in quote marks?",reply_markup=TypesAnswers)
    bot.Sub_state = 'Q5'
    
def Data_TypesAnswer1(message):
    if message.text.lower() == 'integer':
        bot.results += 1   
        bot.send_message(message.chat.id, f"Well done, that is right. 4 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is Integer try to do other 4",)
        bot.wrong += 1
    

def Data_TypesAnswer2(message):
    if message.text.lower() == 'real':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 3 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is Real try to do other 3",)
        bot.wrong += 1
     

def Data_TypesAnswer3(message):
    if message.text.lower() == 'boolean':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 2 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is Boolean try to do other 2",)
        bot.wrong += 1
     
    
def Data_TypesAnswer4(message):
    if message.text.lower() == 'character':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 1 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is Character try to do other 1",)
        bot.wrong += 1 
     
    
def Data_TypesAnswer5(message):
    if message.text.lower() == 'string':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 0 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is String",)
        bot.wrong += 1
    bot.send_message(message.chat.id, f"In the questions about flowcharts you answered correctly{bot.results} time and incorrectly{bot.wrong} times", )
    bot.send_message(message.chat.id, "Also remember that: VARIABLE - a location in memory in which you can temporaly store a value such as a string or number",)

    bot.Sub_state = 'Init'
    bot.state = 'Init'
    bot.results = 0
    bot.wrong = 0
    

def Searching_algorithmsQuestion1(message):
    bot.send_message(message.chat.id, "BINARY search is relating to composed of of or involving 2 things OR involving a choise between or contition of two alternatives only.")
    bot.send_message(message.chat.id, "If in the list there are 16 number for examen, which number will be examened first (in numbers)?",reply_markup=BubbleAnswers)
    bot.Sub_state = 'Q1'
def Searching_algorithmsQuestion2(message):
    bot.send_message(message.chat.id, "If in the list there are 16 number for examen, which number will be examened second if number which where examined first is 42 (in numbers)?",reply_markup=BubbleAnswers)
    bot.Sub_state = 'Q2'
def Searching_algorithmsQuestion3(message):
    bot.send_message(message.chat.id, "If in the list there are 16 number for examen, which number will be examened third if number which where examined second is 35 (in numbers)?",reply_markup=BubbleAnswers)
    bot.Sub_state = 'Q3'
def Searching_algorithmsQuestion4(message):
    bot.send_message(message.chat.id, "If in the list there are 16 number for examen, which number will be examened forth if number which where examined third is 27 (in numbers)?",reply_markup=BubbleAnswers)
    bot.Sub_state = 'Q4'
def Searching_algorithmsQuestion5(message):
    bot.send_message(message.chat.id,"LINEAR search is arranged in a straight line OR processing from one stage to the next in a single series of steps. Computer will examine all objects in list in  order they stay until find the right object?")
    bot.send_message(message.chat.id, "How many numbers will be examened in list(145, 27, 83, 777, 492, 588, 91, 678, 399, 123) to find number 588?",reply_markup=BubbleAnswers)
    bot.Sub_state = 'Q5'
def Searching_algorithmsQuestion6(message):
    bot.send_message(message.chat.id, "Bubble Sort is an algorithm, which sorts an array by repeatedly comparing adjacent elements and swapping them if they are in the wrong order. The algorithm iterates through the array multiple times, with each pass pushing the largest unsorted element to its correct position at the end. ")
    bot.send_message(message.chat.id, "In the array (5, 1, 3, 2, 4, 6) which numbers will examined first?",reply_markup=numAnswers)
    bot.Sub_state = 'Q6'
def Searching_algorithmsQuestion7(message):
    bot.send_message(message.chat.id, "In the array (5, 1, 3, 2, 4, 6) which numbers will examined second?",reply_markup=numAnswers)
    bot.Sub_state = 'Q7'
def Searching_algorithmsQuestion8(message):
    bot.send_message(message.chat.id, "In the array (5, 1, 3, 2, 4, 6), how numbers will stay after 1 pass?",reply_markup=passAnswers)
    bot.Sub_state = 'Q8'
def Searching_algorithmsQuestion9(message):
    bot.send_message(message.chat.id, "Merge Sort in an algorithm, a divide-and-conquer sorting technique. It breaks down an array into smaller subarrays, sorts them individually, and then merges them back together to create a sorted array.")
    bot.send_message(message.chat.id, "After first merge items will be...?",reply_markup=mergeAnswers)
    bot.Sub_state = 'Q9'
def Searching_algorithmsQuestion10(message):
    bot.send_message(message.chat.id, "After second merge items will be...?",reply_markup=mergeAnswers)
    bot.Sub_state = 'Q10'
    
def Searching_algorithmsAnswer1(message):
    if message.text.lower() == '8':
        bot.results += 1   
        bot.send_message(message.chat.id, f"Well done, that is right. 9 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is 8 try to do other 9",)
        bot.wrong += 1
    

def Searching_algorithmsAnswer2(message):
    if message.text.lower() == '4':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 8 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is 4 try to do other 8",)
        bot.wrong += 1
     

def Searching_algorithmsAnswer3(message):
    if message.text.lower() == '2':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 7 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is 2 try to do other 7",)
        bot.wrong += 1
     
    
def Searching_algorithmsAnswer4(message):
    if message.text.lower() == '1':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 6 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is 1 try to do other 6",)
        bot.wrong += 1 
     
def Searching_algorithmsAnswer5(message):
    if message.text.lower() == '6':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 5 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is 6 try to do other 5",)
        bot.wrong += 1 

def Searching_algorithmsAnswer6(message):
    if message.text.lower() == '5,1':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 4 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is 5,1 try to do other 4",)
        bot.wrong += 1

def Searching_algorithmsAnswer7(message):
    if message.text.lower() == '5,3':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 3 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is 5,3 try to do other 3",)
        bot.wrong += 1
    
def Searching_algorithmsAnswer8(message):
    if message.text.lower() == '1,3,2,4,5,6':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 2 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is 1,3,2,4,5,6 try to do other 2",)
        bot.wrong += 1

def Searching_algorithmsAnswer9(message):
    if message.text.lower() == 'pairs':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 1 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is pairs try to do other 1",)
        bot.wrong += 1
    
def Searching_algorithmsAnswer10(message):
    if message.text.lower() == 'groups':
        bot.results += 1    
        bot.send_message(message.chat.id, f"Well done, that is right. 0 questions left ")  
    else:
        #incorrect.append("shapes") 
        bot.send_message(message.chat.id, "Good efford, but this is not right,the right answer is groups",)
        bot.wrong += 1
    bot.send_message(message.chat.id, f"In the questions about foperators you answered correctly{bot.results} time and incorrectly{bot.wrong} times", )
    bot.send_message(message.chat.id, "Also remember that: Objects can be sorted:",)
    bot.send_message(message.chat.id, "Alphabetically (A-Z) - Addreses ",)
    bot.send_message(message.chat.id, "Most popular to least - Shopping online ",)
    bot.send_message(message.chat.id, "Numerically - Grades ",)
    bot.send_message(message.chat.id, "Reverse (Z-A) - Names/Surnames ",)
    bot.send_message(message.chat.id, "Smallest to biggest - Date ",)
    bot.Sub_state = 'Init'
    bot.state = 'Init'
    bot.results = 0
    bot.wrong = 0


    
def FlowchartsQuestions(message):
    if bot.state == 'Flowcharts':
        bot.send_message(message.chat.id, "Answer the question below, to check you knoewledge about flowcharts.  ", reply_markup = confirmation)
    if bot.state == 'Operators':
        bot.send_message(message.chat.id, "Answer the question below, to check you knoewledge about operators.  ", reply_markup = confirmation)
    if bot.state == 'Data types':
        bot.send_message(message.chat.id, "Answer the question below, to check you knoewledge about data types.  ", reply_markup = confirmation)
    if bot.state == 'Searching algorithms':
        bot.send_message(message.chat.id, "Answer the question below, to check you knoewledge about searching algorithms.  ", reply_markup = confirmation)
                    
def MainRoutine(message):
    if bot.state == 'Init':
        permition(message)
    if bot.state == 'Start':
        ChooseTopic(message)
    if bot.state == 'Flowcharts':
        if bot.Sub_state == 'Init':
            permition(message)
            FlowchartsQuestions(message)
            FlowchartsQuestion1(message)
            
        elif bot.Sub_state == 'Q1':
            FlowchartsAnswer1(message)
            FlowchartsQuestion2(message)
        elif bot.Sub_state == 'Q2':
            FlowchartsAnswer2(message)
            FlowchartsQuestion3(message)           
        elif bot.Sub_state == 'Q3':
            FlowchartsAnswer3(message)
            FlowchartsQuestion4(message)
        elif bot.Sub_state == 'Q4':
            FlowchartsAnswer4(message)
            FlowchartsQuestion5(message)
        elif bot.Sub_state == 'Q5':
            FlowchartsAnswer5(message)
            bot.send_message(message.chat.id, "Continue?", reply_markup=answers1)

    if bot.state == 'Operators':
        if bot.Sub_state == 'Init':
            permition(message)
            FlowchartsQuestions(message)
            OperatorsQuestion1(message)
            
        elif bot.Sub_state == 'Q1':
            OperatorsAnswer1(message)
            OperatorsQuestion2(message)
        elif bot.Sub_state == 'Q2':
            OperatorsAnswer2(message)
            OperatorsQuestion3(message)           
        elif bot.Sub_state == 'Q3':
            OperatorsAnswer3(message)
            OperatorsQuestion4(message)
        elif bot.Sub_state == 'Q4':
            OperatorsAnswer4(message)
            OperatorsQuestion5(message)
        elif bot.Sub_state == 'Q5':
            OperatorsAnswer5(message)
            OperatorsQuestion6(message)
        elif bot.Sub_state == 'Q6':
            OperatorsAnswer6(message)
            OperatorsQuestion7(message)
        elif bot.Sub_state == 'Q7':
            OperatorsAnswer7(message)
            bot.send_message(message.chat.id, "Continue?", reply_markup=answers1)
    if bot.state == 'Data types':
        if bot.Sub_state == 'Init':
            permition(message)
            FlowchartsQuestions(message)
            Data_TypesQuestion1(message)
            
        elif bot.Sub_state == 'Q1':
            Data_TypesAnswer1(message)
            Data_TypesQuestion2(message)
        elif bot.Sub_state == 'Q2':
            Data_TypesAnswer2(message)
            Data_TypesQuestion3(message)           
        elif bot.Sub_state == 'Q3':
            Data_TypesAnswer3(message)
            Data_TypesQuestion4(message)
        elif bot.Sub_state == 'Q4':
            Data_TypesAnswer4(message)
            Data_TypesQuestion5(message)
        elif bot.Sub_state == 'Q5':
            Data_TypesAnswer5(message)
            bot.send_message(message.chat.id, "Continue?", reply_markup=answers1)
    if bot.state == 'Searching algorithms':
        if bot.Sub_state == 'Init':
            permition(message)
            FlowchartsQuestions(message)
            Searching_algorithmsQuestion1(message)
            
        elif bot.Sub_state == 'Q1':
            Searching_algorithmsAnswer1(message)
            Searching_algorithmsQuestion2(message)
        elif bot.Sub_state == 'Q2':
            Searching_algorithmsAnswer2(message)
            Searching_algorithmsQuestion3(message)           
        elif bot.Sub_state == 'Q3':
            Searching_algorithmsAnswer3(message)
            Searching_algorithmsQuestion4(message)
        elif bot.Sub_state == 'Q4':
            Searching_algorithmsAnswer4(message)
            Searching_algorithmsQuestion5(message)
        elif bot.Sub_state == 'Q5':
            Searching_algorithmsAnswer5(message)
            Searching_algorithmsQuestion6(message)
        elif bot.Sub_state == 'Q6':
            Searching_algorithmsAnswer6(message)
            Searching_algorithmsQuestion7(message)
        elif bot.Sub_state == 'Q7':
            Searching_algorithmsAnswer7(message)
            Searching_algorithmsQuestion8(message)
        elif bot.Sub_state == 'Q8':
            Searching_algorithmsAnswer8(message)
            Searching_algorithmsQuestion9(message)
        elif bot.Sub_state == 'Q9':
            Searching_algorithmsAnswer9(message)
            Searching_algorithmsQuestion10(message)
        elif bot.Sub_state == 'Q10':
            Searching_algorithmsAnswer10(message)
            bot.send_message(message.chat.id, "Continue?", reply_markup=answers1)

      

    
        
   


@bot.message_handler(func=MainRoutine,content_types=['text'])
def Empty_function(message):
    pass

bot.polling(none_stop=True, interval=0)
