from models import Database, Table, Row, Column
from typing import List

def READ(row, column_index):
    try:
        value = row.read(column_index)
        print(value)
    except IndexError as e:
        print(e)

def WRITE(row, column_index, value: str):
    try:
        row.write(column_index, value)
        print(f'Written value "{value}" at column {column_index}')
    except IndexError as e:
        print(e)

def WHERE(rows, value: str):
    for i, row in enumerate(rows):
        if value in row.data:
            print(f"Value '{value}' found in row {i}.")

def CREATE_TABLE(database: Database, name: str, num_rows: int, column_names: List[str]):
    if name in database.tables:
        print(f"Table '{name}' already exists.")
        return

    num_columns = len(column_names)
    rows = [Row(num_columns) for _ in range(num_rows)]
    columns = [Column(name) for name in column_names]
    new_table = Table(rows, columns, name)
    database.add_table(new_table)

def execute(operation: str, database: Database):
    parts = operation.split()
    if parts[0].upper() == "READ":
        if parts[1] == "*":
            table_name = parts[2]
            if table_name in database.tables:
                database.tables[table_name].read_all()
            else:
                print(f"Table '{table_name}' not found.")
        else:
            try:
                table_name = parts[1]
                row_index = int(parts[2])
                column_index = int(parts[3])
                if table_name in database.tables:
                    row = database.tables[table_name].get_row(row_index)
                    READ(row, column_index)
                else:
                    print(f"Table '{table_name}' not found.")
            except IndexError:
                print("Error: READ operation requires three arguments: table name, row, and column.")
            except ValueError:
                print("Error: READ operation requires table name, row, and column.")
    elif parts[0].upper() == "WRITE":
        try:
            table_name = parts[1]
            row_index = int(parts[2])
            column_index = int(parts[3])
            value = parts[4]
            if table_name in database.tables:
                table = database.tables[table_name]
                row = table.get_row(row_index)
                WRITE(row, column_index, value)
            else:
                print(f"Table '{table_name}' not found.")
        except IndexError:
            print("Error: WRITE operation requires four arguments: table name, row, column, and value.")
        except ValueError:
            print("Error: WRITE operation requires table name, row, column, and value.")
    elif parts[0].upper() == "WHERE":
        try:
            value = parts[1]
            for table in database.tables.values():
                WHERE(table.rows, value)
        except IndexError:
            print("Error: WHERE operation requires one argument: value.")
    elif parts[0].upper() == "CREATETABLE":
        try:
            table_name = parts[1]
            num_rows = int(parts[2])
            column_names = parts[3:]
            CREATE_TABLE(database, table_name, num_rows, column_names)
        except IndexError:
            print("Error: CREATE TABLE operation requires at least three arguments: table name, number of rows, and column names.")
        except ValueError:
            print("Error: CREATE TABLE operation requires a table name, number of rows, and column names.")
    elif parts[0].lower() == "quit()":
        return False
    else:
        print(f'Invalid operation {parts[0]}')
    return True