Run the program.

Enter a username and password into the respective fields in the Tkinter window.

Click the "Submit" button

For the Database Connection: 
Connection to our MySQL database is done using mysql.connector.

The check_func():
1)Retrieves the entered username and password.
2)Executes a SQL query to fetch a user with matching credentials from the users table.
3)It will display the  messages "Invalid Username / Password / Welcome username" using messagebox as per the data entered.
