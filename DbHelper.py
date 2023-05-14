import pyodbc


class DbHelper:
    _connectionTemplate = 'DRIVER={};SERVER={};DATABASE={};ENCRYPT={};UID={};PWD={}'

    @staticmethod
    def format_connection_string(driver_name: str, server_name: str, db_name: str,
                                 user_name: str, user_password: str, is_encrypted: bool = True) -> str:
        encrypt = 'yes' if is_encrypted else 'no'
        connection_string = DbHelper._connectionTemplate.format(driver_name, server_name, db_name, encrypt, user_name,
                                                                user_password)
        print('Creating connection string: ' + connection_string)
        return connection_string

    @staticmethod
    def connect_to_database(connection_string: str) -> [pyodbc.Connection, pyodbc.Cursor]:
        print('Trying to connect to Database with connection string ' + connection_string)
        db_connection = pyodbc.connect(connection_string)
        print('Connected to database')
        cursor = db_connection.cursor()
        return [db_connection, cursor]

    @staticmethod
    def execute_query(cursor: pyodbc.Cursor, query: str, params: list[str]) -> [list[str], list[pyodbc.Row]]:
        final_query = query.format(*params)
        print('Executing query ' + final_query)
        cursor.execute(final_query)
        column_names = [column[0] for column in cursor.description]
        result = cursor.fetchall()
        print('Query executed. Affected rows: ' + str(len(result)))
        return [column_names, result]

    @staticmethod
    def close_connection(connection: pyodbc.Connection, cursor: pyodbc.Cursor) -> None:
        print('Closing database connection')
        cursor.close()
        connection.close()