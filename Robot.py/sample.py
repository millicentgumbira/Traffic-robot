

import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the employee data
employee_data = {
    "Employee ID": ["E001", "E002", "E003", "E004"],
    "Name": ["Nicole Zonke", "Precious Tendayi", "Michael Dendera", "Millicent Gumbira"],
    "Email": ["nicolezonke@gmail.com", "precioustendayi@gmail.com", "michaeldendera@gmail.com", "millicentlisy@gmail.com"],
    "Basic Salary": [1200, 1500, 1800, 1700],
    "Allowances": [300, 400, 500, 400],
    "Taxi Deduction": [50, 60, 70, 40],
    "NSSA Deduction": [30, 40, 50, 60]
}

# Create a DataFrame from the employee data
df = pd.DataFrame(employee_data)

# Define the email sender and recipient
sender_email = "starlisy7@gmail.com"
sender_password = "StarLisy24//"
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os  # Added to use environment variables for sensitive data

# Define the employee data
employee_data = {
    "Employee ID": ["E001", "E002", "E003", "E004"],
    "Name": ["Nicole Zonke", "Precious Tendayi", "Michael Dendera", "Millicent Gumbira"],
    "Email": ["nicolezonke@gmail.com", "precioustendayi@gmail.com", "michaeldendera@gmail.com", "millicentlisy@gmail.com"],
    "Basic Salary": [1200, 1500, 1800, 1700],
    "Allowances": [300, 400, 500, 400],
    "Taxi Deduction": [50, 60, 70, 40],
    "NSSA Deduction": [30, 40, 50, 60]
}

# Create a DataFrame from the employee data
df = pd.DataFrame(employee_data)

# Define the email sender and recipient
# Use environment variables to store sensitive data securely
sender_email = os.getenv("SENDER_EMAIL")  # Changed to fetch from environment variable
sender_password = os.getenv("SENDER_PASSWORD")  # Changed to fetch from environment variable

if not sender_email or not sender_password:
    raise ValueError("Please set the SENDER_EMAIL and SENDER_PASSWORD environment variables.")

# Loop through each employee and send an email
for index, row in df.iterrows():
    employee_id = row['Employee ID']
    name = row['Name']
    email = row['Email']
    basic_salary = row['Basic Salary']
    allowances = row['Allowances']
    taxi_deduction = row['Taxi Deduction']
    nssa_deduction = row['NSSA Deduction']

    # Calculate net salary
    net_salary = basic_salary + allowances - taxi_deduction - nssa_deduction

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = "Payslip for " + name

    # Add the payslip details to the message
    body = f"Employee ID: {employee_id}\nName: {name}\nEmail: {email}\nBasic Salary: {basic_salary}\nAllowances: {allowances}\nTaxi Deduction: {taxi_deduction}\nNSSA Deduction: {nssa_deduction}\nNet Salary: {net_salary}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        print(f"Email sent to {email}")
    except Exception as e:
        # Added exception handling to catch and log errors
        print(f"Failed to send email to {email}. Error: {e}")

# Loop through each employee and send an email
for index, row in df.iterrows():
    employee_id = row['Employee ID']
    name = row['Name']
    email = row['Email']
    basic_salary = row['Basic Salary']
    allowances = row['Allowances']
    taxi_deduction = row['Taxi Deduction']
    nssa_deduction = row['NSSA Deduction']

    # Calculate net salary
    net_salary = basic_salary + allowances - taxi_deduction - nssa_deduction

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = "Payslip for " + name

    # Add the payslip details to the message
    body = f"Employee ID: {employee_id}\nName: {name}\nEmail: {email}\nBasic Salary: {basic_salary}\nAllowances: {allowances}\nTaxi Deduction: {taxi_deduction}\nNSSA Deduction: {nssa_deduction}\nNet Salary: {net_salary}"
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, email, msg.as_string())
    server.quit()

    print(f"Email sent to {email}")
