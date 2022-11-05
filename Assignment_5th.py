def register():
  global username
  username=input("Register your email id : ")
  username_rules="^[a-zA-Z][\w.-]*[@][a-z 0-9]+[.][a-z][\w]{1,3}"
  db=open('user_details.txt','r')
  details()
  if username not in email:
    if re.search(username_rules,username):
      password()
    else:
      print("Try Again with different username")
      register()
  else:
    print("username already exit. Please log with existing email id")
    db.close()
    login()



def password():
  global pd
  pd=input("Enter your password : ")
  pd_rules="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&]{5,16}"
  if re.search(pd_rules,pd):
    confirm_password()
  else:
    print("please enter password with atleast one capital letter,one integer and one special character")
    password()



def confirm_password():
  confirm_pd=input("confirm password : ")
  if pd==confirm_pd:
    db=open('user_details.txt','a')
    db.writelines(username+", "+pd+ "\n")
    print(" registration is successfully")
  
    db.close()
  else:
    print("password is not match, Try again")
    password()


def login():
  global data
  username=input ("Enter your username to login : ")
  Password= input(" Enter password or forgot password : pd | forgot ")
  if Password=="pd":
    pd= input("Please Enter your password : ")
    db=open('user_details.txt','r')
    details()
    try:
      if data[username]:
        if pd==data[username]:
          print("Hi")
          print("Welcome ", username) 
          db.close()
        else:
          print("enter correct password")
          login()
      else:
        print("user id does not exist")
    except:
      print("user id does not exist")
      register()
    
  elif Password=="forgot":
    forgot_pd()
  else:
    print("choose any of the one")
    login()

def forgot_pd():
  username=input("Enter your email id : ")
  try:
      if data[username]:
        db=open('user_details.txt','r')
        details()
        print("the password is ",data[username])
        db.close()
        login()
      else:
        print("user id does not exist")
        register()
  except:
    print("user id does not exist")
    register()

def details():
  global email
  global PD
  global data
  email=[]
  PD=[]
  db=open('user_details.txt','r')
  for i in db:
    x,y=i.split(", ")
    y=y.strip()
    email.append(x)
    PD.append(y)
    data = dict(zip(email,PD))

def select():
  welcome= input("For accessing you need to login and if new user than you need to register in as L | R ")
  if welcome=="R":
    register()
  elif welcome=="L":
    login()
  else:
    print(" choose any one in R | L")
    select()


db=open('user_details.txt','a')
import re
select()