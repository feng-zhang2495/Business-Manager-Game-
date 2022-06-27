import time as t
import random 

#Defining functions so that it's easier later to call on a function multiple times instead of writing it out.

#Prints final results
def final_results():
  print("*"*20) 
  print("FINAL RESULTS:")
  print("*"*20) 
  print(f'You finished the game with ${currentmoney}, you had {permcustomer} permanent customers, a slogan score of {slogan_score}, a customer limit of {customer_limit}, and you gained ${customer_earnings} from your customers.')

#Prints the title of the weekly result
def week_result_title():
  print("") 
  print("*"*15)
  print('WEEK RESULTS:')
  print("*"*15)

#Prints the special event titles
def special_event_title():
  print("")
  print("*"*15)
  print("SPECIAL EVENT:")
  print("*"*15)
  print("") 

#Used when user doesn't have enough money
def not_enough_money():
  print(f"\nYou dont have enough money! You currently have ${currentmoney}.\n")
  t.sleep(2)

#introduction
print('Welcome to Business Manager!')

rules = input('\nWould you like to read the rules of the game?(yes/no)\n')

#Rules
if rules.lower().strip() == 'yes':
  print("**"*30)
  print('In this game you are managing your own business.\n')
  t.sleep(2)
  print('You will start with $1000, 5 regular customers, a "slogan score" of 0, and a customer capacity of 10.\n')
  t.sleep(2)
  print('In this game, money allows you purchase new items to help expand your business.\n')
  t.sleep(2)
  print('Every week, one or two new customers visit your business. Your slogan score determines the likelyhood of a new customer becoming a permanent customer.\n')
  t.sleep(3)
  print('The more customers you have, the more money you will make. Your customer capacity is the maximum amount of customers you can have in your store.\n')
  t.sleep(3)
  print('Each week, you will have to pay a base rent of $200 to keep your business alive. Increasing your customer capacity will also increase your rent fees.')
  t.sleep(3)
  print('\nYou will get to perform a specific action every week:\n')
  t.sleep(2)
  print('1. Increase slogan score (Costs $150)\n')
  t.sleep(2)
  print('2. Expand business size (Increases customer capacity)\n')
  t.sleep(2)
  print('3. Advertisement (Gain or lose a random number of customers temporarily for the week\n')
  t.sleep(2)
  print('4. Work for the company (Gains a random amount of money for the company each week\n')
  t.sleep(2)
  print('The objective of this game is to save $3000 in your bank by week 15, and pay rent through the way, otherwise you lose.') 
  t.sleep(3)
  print('\nP.S. There may be random events that happen throughout the game that can either help or ruin your business.\n')
  t.sleep(2)
  print('Good luck!')
  print("**"*30) 
  t.sleep(2) 

  print('\nPress any key once you have finished reading the rules')
  finishedrules = input("")


#Popular first/last names for the customer name generation
fnames = 'Emma Olivia Ava Isabella Sophia Charlotte Mia Amelia Harper Evelyn Abigail Emily Elizabeth Mila Ella Avery Sofia Camila Aria Scarlett Victoria Madison Luna Grace Chloe Penelope Layla Riley Zoey Nora Lily Eleanor Hannah Lillian Addison Aubrey Ellie Stella Natalie Zoe Leah Hazel Violet Aurora Savannah Audrey Brooklyn Bella Claire Skylar Liam Noah William James Oliver Benjamin Elijah Lucas Mason Logan Alexander Ethan Jacob Michael Daniel Henry Jackson Sebastian Aiden Matthew Samuel David Joseph Carter Owen Wyatt John Jack Luke Jayden Dylan Grayson Levi Isaac Gabriel Julian Mateo Anthony Jaxon Lincoln Joshua Christopher Andrew Theodore Caleb Ryan Asher Nathan Thomas Leo'

lnames = 'Smith Johnson Williams Jones Brown Davis Miller Wilson Moore Taylor Anderson Thomas Jackson White Harris Garcia Martinez Robinson Clark Rodriguez Lee Walker Xu Wang Hall Allen Young King Wright Stewart Da Wong Lu Chen Chan Nguyen Zhao' 

#Puts the names into lists where I can choose them randomly
fname = fnames.split() 
lname = lnames.split() 

#A list of stuff customers are able to buy
furniture = ['Couch', 'Chair', 'Lamp', 'Pencil case', 'Water bottle', 'Pencil', 'Crayon', 'Chromebook', 'Justin Bieber Poster', 'Book', 'Keyboard', 'Textbook', 'Headset', 'Banana', 'Suspicious Oceanic Fish', 'Apple']  

#Sets a random week for which special events happen
eventweek1 = random.randint(3,13)
eventweek2 = random.randint(3,13)
eventweek3 = random.randint(3,13) 

#Makes sure the event weeks are not on the same week 
while eventweek1 == eventweek2:
  eventweek2 = random.randint(3,13)
  
while eventweek1 == eventweek3 or eventweek2 == eventweek3:
  eventweek3 == random.randint(3,13) 

#First while loop loops the entire game, so that the user can play again if they wish 
while True: 

  #Base variables later used in the program
  customer_earnings = 0
  slogan_score = 0
  currentmoney = 1000
  baserent = 200
  permcustomer = 5
  customer_limit = 10
  tempcustomer = random.randint(1,2) 
  admoney = 80
  sloganmoney = 150
  temp_add = 0
  newpermcustomer = 0
  eventweek = random.randint(1,30) 
  daily_income = 0
  
  #This is the loop of the 'main' game: it loops 15 times, as the game is max 15 weeks long.
  for week in range(1,16):

    #The introduction to every new week
    print("")
    print("**"*12)
    print(f'It is currently week {week}.')
    print("**"*12)
    print("") 
    t.sleep(1)

    print(f'What would you like to do?\n')
    t.sleep(1)

    #Calculates the money you have at the start of each week
    week_starting_money = currentmoney

    #The loop for different choices you can do at the start of every week 
    while True:

      #This loop Excepts an error and lets the user reenter a proper number so that they don't have to restart the game
      while True:
        try:
          choice = int(input('1. Increase Slogan Score\n(Increases possibility of a temporary customer becoming a permanent customer, -$200)\n\n2. Expand Business Size\n(+5 Customer space, +$100 rent)\n\n3. Advertise\n(Temporarily gains or loses customers, -$80)\n\n4. Work (Gains a random amount of money for the company)\n'))  
          t.sleep(1)
          break

        except:
          ValueError
          print('\nPlease enter an integer!')
          t.sleep(2)
          continue

      #If statements telling the program what to do in every action the user selects. 
      if choice == 1:  

        #If the user does not have enough money to purchase the program, they will be sent back to choose a different action
        if currentmoney < 150:
          not_enough_money()
          continue
        
        #Output and calculation of currentmoney and slogan score. 
        slogan_score = slogan_score+1.5
        print(f'\nYou now have a {slogan_score}% chance of a temporary customer becoming a permanent customer.\n-$150.\n')
        t.sleep(2)
        currentmoney = currentmoney - baserent - sloganmoney + daily_income
        break

      elif choice == 2:

        #Output and calculation of customer limit and rentcost. 
        customer_limit += 5
        print(f'\nYou now have a customer_limit of {customer_limit}.\n+$100 rent.\n')
        t.sleep(2) 
        baserent += 100
        currentmoney = currentmoney - baserent + daily_income
        break

      elif choice == 3:

        #Output and calculation of currentmoney and new temporary customers. Considers current money too 
        if currentmoney < 80:
          not_enough_money()
          continue

        temp_add = random.randint(-2,4)

        #3 different outputs dependent on how many temporary customers the ad gets.
        if temp_add == 0:
          print(f'\nYour billboard was neither effective nor effective.\n+{temp_add} temporary customers')
          t.sleep(2)
          currentmoney = currentmoney - baserent - admoney + daily_income
          break

        elif temp_add < 0:
          print(f'\nYour billboard was very ineffective...\n{temp_add} temporary customers')
          t.sleep(2)
          currentmoney = currentmoney - baserent - admoney 
          daily_income
          break

        else: 
          print(f'\nYour billboard was very effective!\n+{temp_add} temporary customers')
          t.sleep(2)
          currentmoney = currentmoney - baserent - admoney +daily_income
          break
      
      elif choice == 4:
        work_money = random.randint(-7, 120)

        #Many different outputs dependent on what random number the work money variable is assigned to. These outputs all calculate current money. 
        if work_money < 0:
          print(f'\nInstead of working this week, you bought a muffin. -${-work_money}\n')
          currentmoney = currentmoney - baserent + work_money + daily_income
          t.sleep(2)
          break

        elif work_money == 0:
          print('\nYou did little to nothing today. +$0.\n')
          currentmoney = currentmoney - baserent + work_money
          t.sleep(2)
          break

        elif work_money > 0 and work_money < 15:
          print(f'\nYou found a ${work_money} bill on the floor today.\n') 
          currentmoney = currentmoney - baserent + work_money +daily_income
          t.sleep(2)
          break

        elif work_money >= 15 and work_money < 30:
          print(f'\nYou earned +${work_money} while being constantly distracted by www.thisisnotavirus.com.\n') 
          currentmoney = currentmoney - baserent + work_money + daily_income
          t.sleep(2)
          break
        
        elif work_money >= 30 and work_money < 50:
          print(f'\nYou worked well for 2 hours, earning +${work_money}. After, you had to take care of an ant infestation.\n') 
          currentmoney = currentmoney - baserent + work_money + daily_income
          t.sleep(2)
          break

        elif work_money >= 50 and work_money < 70:
          print(f'\nA wild fly enters your office today, buzzing through your ears, lowering productivity +${work_money}.\n')
          currentmoney = currentmoney - baserent + work_money + daily_income
          t.sleep(2)
          break
        
        elif work_money >= 70 and work_money < 90:
          print(f"\nYou're feeling great today. Nothing can get in the way of your work and you gain +${work_money}.\n")
          currentmoney = currentmoney - baserent + work_money + daily_income
          t.sleep(2)
          break
        
        elif work_money >= 90 and work_money <= 110:
          print(f'\nYou take out the trash in the morning and see your annoying neighour Stacy. You make an excuse: "I have to go to work", and work over the clock +${work_money}.\n')
          currentmoney = currentmoney - baserent + work_money + daily_income
          t.sleep(2)
          break

        else:
          print(f'\nYou take part in a clinical trial of a new "EleKTriK Energy drink" and begin to question its effects... +${work_money}.') 
          currentmoney = currentmoney - baserent + work_money + daily_income
          t.sleep(2)
          break

      #Lets player choose again instead of ending the game if they accidentally press a wrong number. 
      else:
        print('\nPlease enter 1, 2, 3, or 4!\n')
        t.sleep(1)
        continue

    #SPECIAL EVENT #1 
    while eventweek1 == week:
      special_event_title()
      print('Gordon Ramsay is in town and he is willing to help fund your business for the long run! He first wants a loan of a random integer between $500 - $800.')
      t.sleep(3)

      #The price Gordon needs
      loanprice = random.randint(500, 800)

      #Filters out users who don't have enough money to participate in the first place
      if currentmoney < 500:
        print("\nSorry, you didn't have enough money to participate in this event.\n") 
        break 

      #Lets user decide if they wish to pay Gordon Ramsay 
      decision = input('\nDo you wish to pay Gordon Ramsay at least $500? (yes/no)\n\nBe Careful, if you are not able to pay rent fees, you will lose the game!\n')  
      if decision.lower().strip() == 'yes':
        pass
      
      elif decision.lower().strip() == 'no':
        break
      
      decision_money = 500

      #Loop that lets user increase the loan price by $50 until the price is greater than "loan price"
      while True:
        loanchoice = input(f'\nGordon Ramsay says:"${decision_money} is not quite enough..."\n\nWould you like to add $50 to your loan price? (y/n)\n')

        t.sleep(1)

        if loanchoice.lower().strip() == 'yes' or 'y':
          
          decision_money = decision_money + 50

          #If at one point the user runs out of money, this ends the program 
          if decision_money > currentmoney:
            print('\nYou dont have enough money to do that...')
            t.sleep(2)
            break 
          
          #When the money the user gives is greater than or equal to the price gordon is asking for, Gordon will provide the user with a random daily income every week until week 15
          elif decision_money >= loanprice:
            daily_income = random.randint(90,130)  

            #Output
            print(f'\nCongradulations! Gordon Ramsay will be funding your business every week with ${daily_income}!')
            t.sleep(3)
            print(f'-${decision_money}\n') 

            #Calculations
            currentmoney = currentmoney - decision_money + daily_income 
            break 
      
          #If the user decides at one point that the price is too high
          elif loanchoice.lower().strip() == 'no' or 'n':
            break

      
      #If the they paid Gordon Ramsay in the previous loop
      if decision_money >= loanprice:
        break

      #If they did not or gave up on paying Gordon last turn
      elif decision_money < loanprice:
        print('\nGordon is leaving town now...\n') 
        break

    #SPECIAL EVENT #2
    while eventweek3 == week:
      special_event_title()
      print('A DUCK is flying towards your office! Quick, type out the phrase:\n"A duck, duck!"')
      t.sleep(2) 

      #Small countdown before telling user to count
      for i in range(5,0,-1):
        print(i)
        t.sleep(1)
      print('\nType!') 
      
      #Timer starts keeping track of how long the user takes to input the sentence
      time_limit = 5
      start_time = t.time()

      duckstatement = input("")

      #Calculates elapsed time
      elapsed_time = t.time()-start_time

      #If they typed everything correctly and below the time limit
      if duckstatement.lower().strip() == 'a duck, duck!' and elapsed_time <= time_limit:
        
        #Calculations and output
        print('\nYou managed to type the statement correctly and fast enough.')
        t.sleep(2)

        #Duck provides a basic everyday income
        duckincome = random.randint(50,70)
        daily_income = daily_income + duckincome
        print(f'\nYou captured the duck and find that it lays gold eggs.\n+${duckincome} everyday.')

        currentmoney = currentmoney + daily_income
        break
      
      #If the user failed to type the sentence in time or, made spelling errors
      else:

        #Calculations and output
        medicalbill = random.randint(70,110) 
        print(f'\nThe duck hits your face and you have to pay ${medicalbill} in medical bills.') 
        currentmoney = currentmoney - medicalbill
        break

    #SPECIAL EVENT #3
    while eventweek3 == week:
      special_event_title() 

      #Explains the event
      print('\nA tornado cuts a destructive path all through your city. You have the choice of helping the citizens in your city or minding your own business. Do you want to help? (y/n)')
      help = input()
      t.sleep(3)
      
      #If the user decides they want to help the citizens
      if help.lower().strip() == 'y' or 'yes':

        #This loop lets users renenter a valid number if they accidentally entered a string or soemthing invalid
        while True:
          try:
            helpamount = int(input('\nHow much money do you want to give to your citizens?\n'))
            t.sleep(1)
            break

          except:
            ValueError
            print('\nPlease enter an integer answer!')
            t.sleep(2)
            continue

        #Calculations and output 
        merit = round(helpamount/40, 2)
        print(f'\nThe citizens are grateful that you helped them through the crsis. They are {slogan_score*merit}% more likely to become permanent customers!')

        t.sleep(3)
        slogan_score = slogan_score + slogan_score*merit
        currentmoney = currentmoney - helpamount 
        break

      #If they did not help the citizens 
      elif help.lower().strip() == 'n' or 'no':

        #Output
        print('\nYou did not help the citizens.')
        t.sleep(2) 
        break

    #Adds the temporary customers to the permanent customers and also the temporary customers gained from the advertisement to the total customers. 
    totalcustomer = permcustomer + tempcustomer + temp_add

    #If the total amount of customers exceeds the customer limit, this will calculate and remove some customers from the business. 
    if totalcustomer > customer_limit:
      print('\nYou have too many customers this week!')
      t.sleep(1)
      print(f'\n...Kicking out {totalcustomer-customer_limit} customers...')
      t.sleep(2) 
      totalcustomer = customer_limit

    #Output
    print(f'\nThis week, you have {totalcustomer} customers.')
    t.sleep(2) 

    #This loop takes the amount of customers that buys items and computes current cost and the total money made from the customers over the course of the game. 
    for x in range(0, totalcustomer):

      #What the customer is willing to spend
      customer_spend = random.randint(30,70) 

      #Generates a random first and last name from the lists above and creates a customer variable. 
      customer = f'{random.choice(fname)} {random.choice(lname)}'

      #Generates a random item from the list of items that customers can buy 
      buy = random.choice(furniture)

      #Output
      print(f'\n{customer} has bought a {buy} for ${customer_spend}!\n+${customer_spend}') 

      #Calculations
      currentmoney = customer_spend + currentmoney 
      t.sleep(0.5) 
      customer_earnings = customer_earnings + customer_spend

      #Determines the rate of a new permanent customer using slogan score
      if newpermcustomer == 0:
        chance_new_permcustomer = random.randint(1,100)

        #This is the percentage 
        if chance_new_permcustomer <= slogan_score:

          #Output and Increment statements 
          print(f'\n{customer} has become a new permanent customer!') 
          t.sleep(2)
          permcustomer += 1
          newpermcustomer += 1

    #Output results from the week 
    week_result_title()  

    t.sleep(1)
    print(f'\nThis week you started with ${week_starting_money}, currently have ${currentmoney} saved, {permcustomer} permanent customers, {slogan_score} slogan score, a rent fee of ${baserent} and a {customer_limit} customer limit.')
    t.sleep(2) 

    #Resets these temporary variables back to their base value for the next round
    newpermcustomer = 0
    totalcustomer = permcustomer - temp_add
    temp_add = 0
    
    #These if statements determine if the user has won or lost based on the round and the money they have, and they also print the final results of the game
    if week == 15:

      if currentmoney >= 3000:
        print(f"\nCongradulations! You are a true business master you've won with ${currentmoney-3000} extra!")

        final_results()
        break

      elif currentmoney < 3000:
        print(f"\nUnfortunately, you were able to keep your business empire alive, and you needed ${3000-currentmoney} more to win.\n") 

        final_results()
        break
      
    elif currentmoney >= 3000:
      print(f"\nCongradulations! You are a true business master, you've won with {15-week} weeks to spare. Nice job!\n") 

      final_results()
      break 
    
    elif currentmoney < 0:
      print(f'\nUnfortunately, you were not able to pay your rent, your business lasted {week} weeks.') 

      final_results()
      break
    
    #This small imput lets the user read the weekly results before having the next week come up.
    user_input = input('\nPress Enter to continue.')

    if user_input == "\n":
      continue 
  
  #Gives the user a choice to play again 
  choice = input('\nWould you like to play again? (yes/no)\n')

  if choice.lower().strip() == 'yes':
    continue
  
  elif choice.lower().strip() == 'no':
    break
    
  else:
    print('\nPlease enter a valid option') 
    t.sleep(2) 
    break

#Outro 
print('\nThanks for playing the game!') 