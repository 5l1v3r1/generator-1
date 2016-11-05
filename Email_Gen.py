#Getting variables

firstname = raw_input("First Name: ") 

lastname = raw_input("Last Name: ")

print("Enter domain address.  For example, 'github.com': ")
company = raw_input("Domain: ")

#changes semicolon vs comma demarcation
emailprogram = input("What email program are you using? (0 for Gmail, 1 for Outlook)  \n")

#getting first and last letters of names

ffletter = firstname[:1]
lfletter = lastname [:1]


if emailprogram == 0:
	demarcation = ","
else:
	demarcation = ";"

#printing
print("\n")
print("Send email as follows and check which emails bounced")
print("If fewer than 10 bouces something went through")
print("\n")

print("Send Field : ")
print(ffletter+lastname+"@"+company+demarcation+"\n")
print("BCC Field : ")
print(firstname+lastname+"@"+company+demarcation)
print(firstname+"."+lastname+"@"+company+demarcation)
print(lastname+"."+firstname+"@"+company+demarcation)
print(firstname+lfletter+"@"+company+demarcation)
print(lfletter+firstname+"@"+company+demarcation)
print(ffletter+lfletter+"@"+company+demarcation)
print(firstname+"@"+company+demarcation)
print(lastname+"@"+company+demarcation)
print(firstname+"_"+lastname+"@"+company+demarcation)


