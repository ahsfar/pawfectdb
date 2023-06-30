from flask import Flask, render_template, request
import mysql.connector

 

app = Flask(__name__)

 

# Azure MySQL Database Configuration
config = {
    'user': '<your-username>',
    'password': '<your-password>',
    'host': '<your-server-hostname>',
    'database': '<your-database-name>',
    'raise_on_warnings': True
}

 

# Route for the web form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        dog_name = request.form['dog_name']
        email = request.form['email']

 

        # Connect to Azure MySQL Database
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

 

            # Insert data into the 'contacts' table
            sql = "INSERT INTO contacts (name, dog_name, email) VALUES (%s, %s, %s)"
            values = (name, dog_name, email)
            cursor.execute(sql, values)

 

            # Commit changes and close the connection
            conn.commit()
            cursor.close()
            conn.close()

 

            return 'Data has been successfully stored in the database!'
        except mysql.connector.Error as error:
            return 'Error: {}'.format(error)

 

    return render_template('index.html')

 

if __name__ == '__main__':
    app.run()