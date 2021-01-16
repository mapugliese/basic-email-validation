import email_validation

print(email_validation.is_email('@edabit.com'))
# False
print(email_validation.is_email('@edabit'))
# False
print(email_validation.is_email('matt@edabit.com'))
# True
print(email_validation.is_email(''))
# False
print(email_validation.is_email('hello.gmail@com'))
# False
print(email_validation.is_email('bill.gates@microsoft.com'))
# True
print(email_validation.is_email('hello@email'))
#  False
print(email_validation.is_email('%^%$#%^%'))
# False
print(email_validation.is_email('www.email.com'))
# False
print(email_validation.is_email('email'))
# False