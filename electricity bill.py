print("                                            Electricity Bill         ")
print("                                                 CSPDCL                ")

n=int(input("enter number of Unit:"))
if ( 0<n and n<100 or n==100):
     print("You have to pay 2.4/- per hour i.e you need to pay:",n*2.4,"/-")
     
if(101<=n and n<=200):
     x=n-100
     print("You have to pay 2.5/- per hour i.e you need to pay:",x*2.5+(n-x)*2.4,"/-")
               
if (201<=n and n<=400):
     y=n-200
     print("You have to pay 3.2/- per hour i.e you need to pay:",y*3.2+((n-y-100)*2.5)+((n-y-100)*2.4),"/-")
        
if (401<=n and n<=600):
     z=n-400
     print("You have to pay 3.5/- per hour i.e need to pay:",z*3.5+((n-z-200)*3.2)+((n-z-300)*2.5)+((n-z-300)*2.4),"/-")
     
if (601<=n):
     p=n-600
     print("You have to pay 4.85/- per hour i.e need to pay:",p*4.85+((n-p-400)*3.5)+((n-p-400)*3.2)+((n-p-500)*2.5)+((n-p-500)*2.4),"/-")
     
# import datetime
from datetime import datetime
# current date and time
now = datetime.now()

# format date
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Date and Time:",date_time)

print("Thank You , Visit again")
