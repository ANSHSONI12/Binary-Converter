print('Choose an action:')
print('Press 1 to convert decimal to binary')
print('Press 2 to convert binary to decimal')
print('Press 3 to compare binary numbers')
print()
option= int(input('Which would you like to choose:'))#These are your options that are given too you so make sure to write them

def dec_to_bin(num):#for option 1 we have to make the first prediction which will convert the decimal number inputted to a binary
  while num!= 0:#inorder to fo that the wuicker way to do this by moddling it to 2 and appending the reaminder ehich will either be 1 or 0
    remainder= num%2#mod the number by 2 to get the remainder as either 0 or 1
    binary_converstion.append(remainder)#append that to the list
    num= num/2#floor divide the number to shrink it and keep going until it hits 0

if option==1:#for the actual option you first start by making an empty list to store the binary digits
  binary_converstion= []
  num= int(input('Enter a decimal number:'))#get input from the user for what number they want to convert
  dec_to_bin(num)#use the decimal to binary functiob made it at start if the program
  binary_converstion.reverse()#in order to make the list come out correct you need to reverse the list 
  print(str(num)+' = '+str(binary_converstion))#and print out the final results

def split(num):#for the second option i made a procedure which will
  while num>0:
    digits.append(num%10)
    num//=10

def split(num):
  while num>0:
    digits.append(num%10)
    num//=10

def bin_to_dec(digits):
  sum=0
  for i in range(len(digits)):
    sum=sum+digits[i]*pow(2,i)
  print(str(binary1)+'='+str(sum))

if option==2:
  binary= int(input('Enter the binary number you would like to convert:'))
  binary1= binary 
  digits= []
  split(binary)
  bin_to_dec(digits)

def split1(bin1):
  while bin1>0:
    list1.append(bin1%10)
    bin1//=10

def split2(bin2):
  while bin2>0:
    list2.append(bin2%10)
    bin2//=10

def compare(bin1,bin2):
  sum1=0
  sum2=0
  for i in range(len(list1)):
    sum1=sum1+list1[1]*pow(2,i)
  for i in range(len(list2)):
    sum2=sum2+list2[1]*pow(2,i)
  print(str(sum1)+' , '+str(sum2))

if option==3:
  list1=[]
  list2=[]
  bin1 = int(input('Enter a binary Number: '))
  print()
  bin2= int(input('Enter another Binary Number: '))
  split1(bin1)
  split2(bin2)

  compare(bin1,bin2)
  print(str(bin1)+' , '+str(bin2))
  