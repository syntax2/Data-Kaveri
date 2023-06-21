from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Create the "user" table if it doesn't exist
def create_user_table():
    cnx = mysql.connector.connect(user='root', password='secret',
                                  host='db', database='mydb')
    cursor = cnx.cursor()

    # SQL statement to create the "user" table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS `user` (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `name` VARCHAR(255) NOT NULL,
        `email` VARCHAR(255) NOT NULL
    );
    '''

    # Execute the create table query
    cursor.execute(create_table_query)
    cnx.commit()

    cursor.close()
    cnx.close()

@app.route('/home', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        # Retrieve user input from the request
        name = request.form.get('name')
        email = request.form.get('email')

        # Capitalize the first letters of the name
        name = name.title()

        # Connect to MySQL database
        cnx = mysql.connector.connect(user='root', password='secret',
                                      host='db', database='mydb')
        cursor = cnx.cursor()

        # Create the "user" table if it doesn't exist
        create_user_table()

        # Prepare the SQL statement
        sql = "INSERT INTO `user` (name, email) VALUES (%s, %s)"

        # Execute the SQL statement
        cursor.execute(sql, (name, email))
        cnx.commit()

        cursor.close()
        cnx.close()

        return 'Data stored successfully!'

    return '''
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br>
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

