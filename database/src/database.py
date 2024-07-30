import pickle
from models import Row, Column, Table, Database

def save_database(db: Database, filename: str):
    with open(filename, 'wb') as file:
        pickle.dump(db, file)
    print(f"Database saved to {filename}")

def load_database(filename: str) -> Database:
    try:
        with open(filename, 'rb') as file:
            db = pickle.load(file)
        print(f"Database loaded from {filename}")
        return db
    except FileNotFoundError:
        print(f"No existing database found at {filename}. Starting fresh.")
        return Database([])
    except pickle.PickleError:
        print(f"Error loading the database from {filename}. The file might be corrupted.")
        return Database([])

# Define and initialize the database
def initialize_database() -> Database:
    rows1 = [Row(5) for _ in range(3)]
    columns1 = [Column(f'Column {i}') for i in range(5)]
    table1 = Table(rows1, columns1, "Table1")

    rows2 = [Row(4) for _ in range(2)]
    columns2 = [Column(f'Column {i}') for i in range(4)]
    table2 = Table(rows2, columns2, "Table2")

    return Database([table1, table2])

# Initialize the database and save it as a global variable
database = initialize_database()

# Example usage
if __name__ == "__main__":
    save_database(database, 'database.pkl')
    database = load_database('database.pkl')