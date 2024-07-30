from database import database, save_database, load_database
import console
from scripts import execute

# Optionally load the database from a file at the start
database = load_database('database.pkl')

while True:
    command = console.get_command()
    if command.lower() == 'quit()':
        break
    if not execute(command, database):
        break

# Save the database to a file when exiting
save_database(database, 'database.pkl')