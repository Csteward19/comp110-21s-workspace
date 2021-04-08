"""Utility functions for wrangling data."""

__author__ = "730404260"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_open = open(csv_file, "r", encoding="utf8")
    csv_read = DictReader(file_open)
    for row in csv_read:
        rows.append(row)
    file_open.close()
    return rows
   

def column_values(data_rows: list[dict[str, str]], column_name: str) -> list[str]:
    """Shows values for column of data."""
    column_data: list[str] = []
    for dictionary in data_rows:
        column_data.append(dictionary[column_name])
    return column_data


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform from row based to column based data."""
    transform_data: dict[str, list[str]] = {}
    names: dict[str, str] = row_table[0]
    for column in names:
        transform_data[column] = column_values(row_table, column) 
    return transform_data


def head(col_table: dict[str, list[str]], n_rows: int) -> dict[str, list[str]]:
    """Produces table for certain number of rows.""" 
    table_returned: dict[str, list[str]] = {}
    column_names: list[str] = []
    for name in col_table:
        column_names.append(name)
    i = 0
    for subject in range(0, n_rows - 1):
        if i < len(column_names):
            table_returned[column_names[i]] = col_table[column_names[i]]
        i += 1
    return table_returned


def select(select_column: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Selects specific subset of columns."""
    returned_dict: dict[str, list[str]] = {}
    for col_name in names:
        returned_dict[col_name] = select_column[col_name]
    return returned_dict


def count(frequency: list[str]) -> dict[str, int]:
    """Counts for each subject."""
    val_list: dict[str, int] = {}
    for item in frequency:
        if item in val_list:
            val_list[item] += 1
        else:
            val_list[item] = 1
    return val_list