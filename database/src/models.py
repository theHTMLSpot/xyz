from typing import List

class Database:
    def __init__(self, tables: List['Table']) -> None:
        self.tables = {table.name: table for table in tables}

    def add_table(self, table: 'Table') -> None:
        if table.name in self.tables:
            print(f"Table '{table.name}' already exists.")
        else:
            self.tables[table.name] = table
            print(f"Table '{table.name}' created.")

class Table:
    def __init__(self, rows: List['Row'], columns: List['Column'], name: str) -> None:
        self.rows = rows
        self.columns = columns
        self.name = name

    def get_row(self, index: int) -> 'Row':
        while len(self.rows) <= index:
            # Create a new row with the same number of columns as the existing ones
            self.rows.append(Row(len(self.columns)))
        return self.rows[index]

    def read_all(self):
        # Print headers
        headers = [col.head for col in self.columns]
        print(" | ".join(headers))
        # Print rows without row labels
        for row in self.rows:
            print(" | ".join(map(str, row.data)))

class Row:
    def __init__(self, length) -> None:
        self.length = length
        self.data = [None] * length  # Initialize row with None values

    def read(self, column_index: int):
        if 0 <= column_index < self.length:
            return self.data[column_index]
        else:
            raise IndexError("Column index out of range")

    def write(self, column_index: int, value):
        if 0 <= column_index < self.length:
            self.data[column_index] = value
        else:
            raise IndexError("Column index out of range")

class Column:
    def __init__(self, head) -> None:
        self.head = head