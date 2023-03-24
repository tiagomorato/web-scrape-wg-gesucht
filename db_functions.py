import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def db_query(query: str, parameters=False) -> list:
    """
    Executes a SQL query and returns the results.

    :param query: The SQL query to execute.
    :type query: str
    :param parameters: The parameters to use for a parameterized query.
    :type parameters: list, tuple, or None
    :return: A list of tuples representing the result set, or empty list
    :rtype: list
    :raises mysql.connector.Error: If an error occurs during database operations.
    """

    try:
        connection = mysql.connector.connect(
            host=os.environ.get('DB_HOST'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD')
        )

        cursor = connection.cursor()
        cursor.execute(query, parameters)

        # if the query is a insert/update/delete statement (even if parameterized),
        # return the number of rows affected
        if cursor.with_rows:
            result = cursor.fetchall()
        else:
            result = cursor.rowcount

        # print("Rows affected: ", result)

        connection.commit()
        cursor.close()
        connection.close()

        return result

    except mysql.connector.Error as error:
        print(f"Error executing query: {error}")
        raise


def db_create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS wg_berlin (
        data_id INT NOT NULL,
        title VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL,
        price VARCHAR(255) NOT NULL,
        size VARCHAR(255) NOT NULL,
        flatmate VARCHAR(255) NOT NULL,
        available VARCHAR(255) NOT NULL,
        on_since VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        link TEXT NOT NULL,
        insert_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(data_id)
    );
    """

    return db_query(sql)
