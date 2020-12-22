responses=["Welcome to smart calculator","My name is Ditto","Thanks","Sorry,this is beyond my ability"]

def extract_numbers_from_text(text):
       l=[]
       for t in text.split(' '):
              try:
                     l.append(float(t))
              except ValueError:
                     pass
       return(l)
def lcm(a,b):
       L=a if a>b else b
       while L<=a*b:
              if L%a==0 and L%b==0:
                  return L
              L=L+1
def hcf(a,b):
       H=a if a<b else b
       while H>=1:
              if a%H==0 and b%H==0:
                     return H
              H=H-1
def add(a,b):
       return(a+b)
def sub(a,b):
       return(a-b)
def multiply(a,b):
       return (a*b)
def division(a,b):
       return (a/b)
def dollar_in_rs(dollar):
       rupees=dollar*64
       return rupees
def factorial(num):
       if n==1:
              return num
       else:
              return num*factorial(num-1)


def end():
       print(responses[2])
       input("Press enter key to exit")
       exit()
def myname():
   print(responses[1])
def sorry():
   print(responses[3])
operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"MINUS":sub,"SUBTRACTION":sub,"SUBTRACT":sub
            ,"DIVIDE":division,"DIVISION":division,"LCM":lcm,"HCF":hcf,"rs":dollar_in_rs,"dollar in rs":dollar_in_rs,"factorial":factorial,"fact":factorial}
            
commands={"NAME":myname,"END":end,"CLOSE":end}
