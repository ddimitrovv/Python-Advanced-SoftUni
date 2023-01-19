# You will be given some emails until you receive the command "End".
# Create the following custom exceptions to validate the emails:
#     • NameTooShortError - raise it when the name in the email is less than or equal to 4
#       ("peter" will be the name in the email "peter@gmail.com")
#     • MustContainAtSymbolError - raise it when there is no "@" in the email
#     • InvalidDomainError - raise it when the domain of the email is invalid
#       (valid domains are: .com, .bg, .net, .org)
# When an error is encountered, raise it with an appropriate message:
#     • NameTooShortError - "Name must be more than 4 characters"
#     • MustContainAtSymbolError - "Email must contain @"
#     • InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
# Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
# If the current email is valid, print "Email is valid" and read the next one

from custom_exeptions import MustContainAtSymbolError, NameTooShortError, InvalidDomainError


def check_if_at_in_email(email):
    email = email.split('@')
    if len(email) != 2:
        raise MustContainAtSymbolError('Email must contain @')


def check_username_len(email):
    username, domain = email.split('@')
    if len(username) < 5:
        raise NameTooShortError('Name must be more than 4 characters')


def check_domain(email):
    valid_domains = {
        '.com',
        '.bg',
        '.net',
        '.org',
    }
    domain = '.' + email.split('.')[-1]
    if domain not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')


while True:

    email_to_validate = input()

    if email_to_validate == 'End':
        break

    check_if_at_in_email(email_to_validate)
    check_username_len(email_to_validate)
    check_domain(email_to_validate)
    print('Email is valid')
