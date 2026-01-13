print()
print('Online International Flight Booking')
Day = input('Enter the day : ').lower()
if 'a' in Day :
   print('Available Internasional Flights : ')
   print('A. (09.00) Indonesia - Philippines ')
   print('B. (07.15) Indonesia - Malaysia')
   print('C. (08.30) Indonesia - Thailand')
   print('D. (06.40) Indonesia - Brunei')
   print('E. (05.50) Indonesia - Vietnam')
   print('F. (07.45) Indonesia - Myanmar')
   print('G. (09.45) Indonesia - Cambodia')
   print('H. (06.25) Indonesia - Laos')
   print('I. Exit')
   pack1 = input('Flight you want to attend : ').lower()
   while pack1 != 'i' :
       if 'a' in pack1 :
           code = 'PH0900'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 9.000.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'b' in pack1 :
           code = 'MY0715'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 7.150.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'c' in pack1 :
           code = 'TL0830'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 8.300.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'd' in pack1 :
           code = 'BR0640'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 6.400.000')
           pay = input('Do you accept the offer (yes/no) : '). lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'e' in pack1 :
           code = 'VE0550'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 5.500.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'f' in pack1 :
           code = 'MM0745'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 7.450.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'g' in pack1 :
           code = 'CB0945'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 9.450.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'h' in pack1 :
           code = 'LS0625'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 6.250.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       else :
           break
           
elif 'b' in Day :
   print('Available Internasional Flights : ')
   print('A. (11.50) Indonesia - Philippines ')
   print('B. (13.00) Indonesia - Malaysia')
   print('C. (12.15) Indonesia - Thailand')
   print('D. (12.45) Indonesia - Brunei')
   print('E. (14.00) Indonesia - Vietnam')
   print('F. (13.30) Indonesia - Myanmar')
   print('G. (14.25) Indonesia - Cambodia')
   print('H. (11.35) Indonesia - Laos')
   print('I. Exit')
   pack2 = input('Flight you want to attend : ')
   while pack2 != 'i' :
       if 'a' in pack2 :
           code = 'PH1150'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 11.500.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'b' in pack2 :
           code = '1300'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 13.000.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'c' in pack2 :
           code = 'TL1215'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 12.150.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'd' in pack2 :
           code = 'BR1245'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 12.450.000')
           pay = input('Do you accept the offer (yes/no) : '). lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'e' in pack2 :
           code = 'VE1400'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 14.000.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'f' in pack2 :
           code = 'MM1330'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 13.300.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'g' in pack2 :
           code = 'CB1425'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 14.250.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'h' in pack2 :
           code = 'LS1135'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 11.350.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       else :
           break
           
elif 'c' in Day :
   print('Available Internasional Flights : ')
   print('A. (15.15) Indonesia - Philippines ')
   print('B. (16.05) Indonesia - Malaysia')
   print('C. (16.40) Indonesia - Thailand')
   print('D. (17.25) Indonesia - Brunei')
   print('E. (18.00) Indonesia - Vietnam')
   print('F. (17.05) Indonesia - Myanmar')
   print('G. (15.45) Indonesia - Cambodia')
   print('H. (19.15) Indonesia - Laos')
   print('I. Exit')
   pack3 = input('Flight you want to attend : ')
   while pack3 != 'i' :
       if 'a' in pack3 :
           code = 'PH1515'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 15.150.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'b' in pack3 :
           code = 'MY1605'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 16.050.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'c' in pack3 :
           code = 'TL1640'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 16.400.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'd' in pack3 :
           code = 'BR1725'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 17.250.000')
           pay = input('Do you accept the offer (yes/no) : '). lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'e' in pack3 :
           code = 'VE1800'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 18.000.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'f' in pack3 :
           code = 'MM1705'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 17.050.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'g' in pack3 :
           code = 'CB1545'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 15.450.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       elif 'h' in pack3 :
           code = 'LS1915'
           firstname = input('Enter Your First Name : ').upper()
           lastname = input('Enter Your Last Name : ').upper()
           print('Total = Rp 19.150.000')
           pay = input('Do you accept the offer (yes/no) : ').lower()
           if 'yes' in pay :
               print()
               print('Your Flight',code,firstname,lastname)
               import time
               t = time.localtime(time.time())
               localtime = time.asctime(t)
               str = "Transaction Time : " + time.asctime(t)
               print(str)
               break
           else :
               print('Thankyou')    
               break
       else :
           break
elif 'sun' in Day :          
     print('No Flights Available')
else :
    print('Error')