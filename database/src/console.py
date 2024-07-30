import datetime
import os


# Getting current datetime
current_datetime = datetime.datetime.now()

# Getting system version
system_version = os.uname().version

# Getting system type
system_type = os.uname().sysname

# Printing the formatted string
print(f'''
    ELQ 3.10.13 ({current_datetime}) [ {system_version} on {system_type}]
    Type "help" for more information
      ''')

# Command input
def get_command():
   command = input("ELQ>")
   return command

