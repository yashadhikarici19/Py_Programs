# 7. WAP that reads a date as an integer int format MMDDYY the program will call a funtion 
# that prints the date in frmat monthname day year 
# eg 122522 -> December 25 2022

x= int(input())

months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 
          7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

print(months[x//10000],(x//100)%100,2000+x%100)