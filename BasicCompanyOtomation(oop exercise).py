import re

from pyparsing import ParseSyntaxException


class Company():
    def __init__(self,companyName):
        self.companyName = companyName
        self.work = True
        
        
        
        
     # define the methods   
    def program(self):
        chose = self.selectionMenu()# When the function calls, it have to use parentheses
        if chose == 1:
            self.addStaff()
        elif chose == 2:
            self.deleteStaff()
        elif chose == 3:
            choice = input('Is the salary monthly or yearly?(m/y)\n')
            while choice !='m'and choice != 'y':
                choice = input('Please enter the yearly(y) or monthly(m):\n')
            if choice == 'm':
                self.showSalary(choice = 'm')
            elif choice == 'y':
                self.showSalary(choice = 'y')
            
            
        elif chose == 4:
            self.paySalary()
        elif chose == 5:
            self.showExpense()
        elif chose == 6:
            self.earnings()
        return chose
    
    def selectionMenu(self):
        chosing = int(input('*** Welcome to {} otomation ***\n\n1-Add Employee\n2-Delete Employee\n3-Show Salary\n4-Pay Salary\n5-Show Expense\n6-Show Earnings\n\nEnter your selection: '.format(self.companyName)))
        while chosing > 6 or chosing<1:
            chosing = int(input('Please, entry selection for 1-6\n'))
        
        return chosing
    
    def addStaff(self):
        
        name = input('Enter the name of the employee: ')
        surname = input('Enter the surname of the employee: ')
        age = input('Enter the age of the employee: ')
        sex = input('Enter the sex of the employee: ')
        salary = input('Enter the salary of the employee:')
               
        
        
        
        
        
        
        with open('employee.txt','r') as file:
            showingEmployee = file.readlines()
            # print(showingEmployee)
        if len(showingEmployee)==0:
            id = 1
        else:
            with open('employee.txt','r') as file:
                id = int(file.readlines()[-1].split(")")[0])+1
                
        with open('employee.txt','a+') as file:
            file.writelines(f'{id}){name}-{surname}-{age}-{sex}-{salary}\n')
        list1 = []
        with open('employee.txt','r') as file:
            list1 =file.readlines()
        for each in list1:
            eachs = each.strip()
            eachs.replace('-',' ')
            print(eachs)
                      
            
            
            
    
    def deleteStaff(self):
        with open('employee.txt','r') as file:
            employees = file.readlines()
            # print(employees)
            
        cEmployee = []    
        for employee in employees:
            new = employee.strip()
            # print(new)
            news = new.replace('-',' ')
            print(news)
           
        number = int(input(f'Please enter the number of the staff which removes from the {company.companyName} company\n'))
        while number<1 or number> len(employees):
            number = int(input(f'Please enter the number between 1-{len(employees)}\n'))
        employees.pop(number-1) 
        
        for eemployee in employees:
            # here = eemployee.strip()
            
            
            cEmployee.append(eemployee.split(')')[1])
        
        id = 0    
        xEmployee =[]
        for employeeee in cEmployee:
            id+=1
            xEmployee.append(f'{id}){employeeee}')
        for again in xEmployee:
            print(again)
        # print(xEmployee)
        with open('employee.txt','w') as file:
            file.writelines(xEmployee)
             
            
    def showSalary(self,choice):
        self.choice = choice
        # print('It is working')
        with open('employee.txt','r') as file:
            employeess = file.readlines()
        # print(employeess)
        sumSalary = []
            
        for employeei in employeess:
            sumSalary.append(int(employeei.split('-')[-1]))
        if self.choice == 'm':
            sumv=sum(sumSalary)
            with open('Expenses.txt','w') as file:
                file.writelines(str(sumv)+'\n')
                print(f'You have to give salary this month :{sumv}')
                
        elif self.choice == 'y':
            sumv = (12*sum(sumSalary))
            with open('Expenses.txt','w') as file:
                file.writelines(str(sumv)+'\n')
                print(f'You have to give salary this year :{sumv}')
        return sumv
             
            
            
                
        
    
    def paySalary(self):
        with open('budget.txt','r') as file:
            pay = file.readlines()[0]
            paySalary1 =int(pay)
        with open('Expenses.txt','r') as file:
            expense = int(file.readlines()[0])
        FinalPay =  paySalary1 - expense
        with open('budget.txt','w') as file:
            file.writelines(str(FinalPay))
        print(FinalPay)
        return paySalary1
        
        
        
    def showExpense(self): 
        otherExpense = int(input('Please enter the sum of the another expense: '))
        with open('Expenses.txt','r') as file:
            expense = int(file.readlines()[0])
        sumExpense = expense+otherExpense
        print(f'Sum of the expenses is {sumExpense}')  
            
    
    def earnings(self):
        earn = int(input('Please enter the earnings of the company:\n'))
        with open('earnings.txt','w') as file:
            file.writelines(str(earn))
        print(f'Sum of the earning is {earn}')
        return earn
    
    # the name of the company
company = Company('Alican Kaplancı') 

while company.work:
    company.program()
    
