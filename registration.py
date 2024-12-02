import mysql.connector
from mysql.connector import Error

# Connect to MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database="Registration_model",
            user='root',
            password='loku'
        )
        if connection.is_connected():
            print("Connected to MySQL")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Create operation (Insert)
def create_registration(name, email, dob, phone, address):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            sql = """INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber, Address) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (name, email, dob, phone, address))
            connection.commit()
            print("Registration created successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Read operation (Select)
def read_registration(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            sql = "SELECT * FROM Registration WHERE ID = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            if result:
                print(f"ID: {result[0]}, Name: {result[1]}, Email: {result[2]}, Date of Birth: {result[3]}, Phone: {result[4]}, Address: {result[5]}")
            else:
                print("Registration not found.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Update operation
def update_registration(id, name=None, email=None, dob=None, phone=None, address=None):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            # Create the SET clause dynamically based on provided fields
            fields = []
            values = []
            if name:
                fields.append("Name = %s")
                values.append(name)
            if email:
                fields.append("Email = %s")
                values.append(email)
            if dob:
                fields.append("DateOfBirth = %s")
                values.append(dob)
            if phone:
                fields.append("PhoneNumber = %s")
                values.append(phone)
            if address:
                fields.append("Address = %s")
                values.append(address)

            # SQL update query
            if fields:
                sql = f"UPDATE Registration SET {', '.join(fields)} WHERE ID = %s"
                values.append(id)
                cursor.execute(sql, tuple(values))
                connection.commit()
                print(f"Registration {id} updated successfully!")
            else:
                print("No fields to update.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Delete operation
def delete_registration(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            sql = "DELETE FROM Registration WHERE ID = %s"
            cursor.execute(sql, (id,))
            connection.commit()
            print(f"Registration {id} deleted successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Example usage:

# Create a new registration
create_registration("John Doe", "john.doe@example.com", "1985-06-15", "1234567890", "123 Elm St.")

# Read registration by ID
read_registration(1)

# Update registration with ID 1
update_registration(1, name="Johnathan Doe", phone="0987654321")

# Delete registration by ID
delete_registration(1)
