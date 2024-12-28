from flask import Flask, request, render_template, redirect
import pandas as pd
import os

app = Flask(__name__)

# Define the path for the Excel file
FILE_PATH = "D:\kuch bhi\SolarSwap\Hackspire\user_data.xlsx"

# Route to render the form
@app.route('/')
def form():
    return render_template("login_sign.html")  # Ensure 'form.html' is the HTML file

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['Username']
    email = request.form['Email']
    phone = request.form['Phone Number']
    address = request.form['Full Address']
    postalCode = request.form['Postal Code']
    city = request.form['City']
    state = request.form['State']
    password = request.form['Password']

    # Check if the Excel file exists
    if not os.path.exists(FILE_PATH):
        # Create a new Excel file with a header row
        df = pd.DataFrame(columns=["Name", "Email", "Phone Number", "Full Address", "Postal Code", "City", "State", "Password"])
        df.to_excel(FILE_PATH, index=False)

    # Load the existing data
    df = pd.read_excel(FILE_PATH)

    # Append new data
    new_data = {"Name": name, "Email": email, "Phone": int(phone), "address" : address, "postalCode" : int(postalCode), "city" : city, "state" : state, "password" : password}
    df = df.append(new_data, ignore_index=True)

    # Save back to the Excel file
    df.to_excel(FILE_PATH, index=False)

    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
