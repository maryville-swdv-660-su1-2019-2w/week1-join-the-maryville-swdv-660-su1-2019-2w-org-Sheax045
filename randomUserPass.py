from mempass import mkpassword
from random_cli import secrets


selection = input('Press Enter to generate a random Username and Password.')

username = mkpassword(1)
password = secrets.token_hex(8)

if selection == '':
    print('Username: {0} '.format(username))
    print('Password: {0}'.format(password))




    