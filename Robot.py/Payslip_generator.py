import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the employee data
data = {
    "Employee ID": ["E001", "E002", "E003", "E004"],
    "Name": ["Nicole Zonke", "Precious Tendayi", "Michael Dendera", "Millicent Gumbira"],
    "Email": ["nicolezonke@gmail.com", "precioustendayi@gmail.com", "michaeldendera@gmail.com", "millicentlisy@gmail.com"],
    "Basic Salary": [1200, 1500, 1800, 1700],
    "Allowances": [300, 400, 500, 400],
    "Taxi Deduction": [50, 60, 70, 40],
    "NSSA Deduction": [30, 40, 50, 60]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the email sender and recipient
sender_email = "starlisy7@gmail.com"
sender_password = "eoji olom dxjn duuc"

# Define the email content
subject = "Payslip for [Employee Name]"
body = """
Dear [Employee Name],

Your payslip details are as follows:

Employee ID: [Employee ID]
Name: [Employee Name]
Email: [Email]
Basic Salary: [Basic Salary]
Allowances: [Allowances]
Taxi Deduction: [Taxi Deduction]
NSSA Deduction: [NSSA Deduction]
Net Salary: [Net Salary]

Best regards,
[GOLDEN STAR INNOVATIONS]
"""

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
    msg['Subject'] = subject

    # Populate the email content with the employee's data
    body = body.replace("[Employee ID]", employee_id)
    body = body.replace("[Employee Name]", name)
    body = body.replace("[Email]", email)
    body = body.replace("[Basic Salary]", str(basic_salary))
    body = body.replace("[Allowances]", str(allowances))
    body = body.replace("[Taxi Deduction]", str(taxi_deduction))
    body = body.replace("[NSSA Deduction]", str(nssa_deduction))
    body = body.replace("[Net Salary]", str(net_salary))

    # Attach the email content to the message
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, email, msg.as_string())
    server.quit()

    # Print payslip details
    print(f"Employee ID: {employee_id}")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Basic Salary: {basic_salary}")
    print(f"Allowances: {allowances}")
    print(f"Taxi Deduction: {taxi_deduction}")
    print(f"NSSA Deduction: {nssa_deduction}")
    print(f"Net Salary: {net_salary}")
    print("------------------------")


import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from fpdf import FPDF  # Added to generate PDF

# Define the employee data
data = {
    "Employee ID": ["E001", "E002", "E003", "E004"],
    "Name": ["Nicole Zonke", "Precious Tendayi", "Michael Dendera", "Millicent Gumbira"],
    "Email": ["nicolezonke@gmail.com", "precioustendayi@gmail.com", "michaeldendera@gmail.com", "millicentlisy@gmail.com"],
    "Basic Salary": [1200, 1500, 1800, 1700],
    "Allowances": [300, 400, 500, 400],
    "Taxi Deduction": [50, 60, 70, 40],
    "NSSA Deduction": [30, 40, 50, 60]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the email sender and recipient
sender_email = "starlisy7@gmail.com"
sender_password = "eoji olom dxjn duuc"

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

    # Generate a PDF for the payslip
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Payslip", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Employee ID: {employee_id}", ln=True)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Basic Salary: {basic_salary}", ln=True)
    pdf.cell(200, 10, txt=f"Allowances: {allowances}", ln=True)
    pdf.cell(200, 10, txt=f"Taxi Deduction: {taxi_deduction}", ln=True)
    pdf.cell(200, 10, txt=f"NSSA Deduction: {nssa_deduction}", ln=True)
    pdf.cell(200, 10, txt=f"Net Salary: {net_salary}", ln=True)

    # Save the PDF
    pdf_filename = f"Payslip_{employee_id}.pdf"
    pdf.output(pdf_filename)

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = f"Payslip for {name}"

    # Add email body
    body = f"Dear {name},\n\nPlease find attached your payslip for this month.\n\nBest regards,\nGOLDEN STAR INNOVATIONS"
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={pdf_filename}',
        )
        msg.attach(part)

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        print(f"Email sent to {email} with payslip attached.")
    except Exception as e:
        print(f"Failed to send email to {email}. Error: {e}")

    # Print payslip details
    print(f"Employee ID: {employee_id}")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Basic Salary: {basic_salary}")
    print(f"Allowances: {allowances}")
    print(f"Taxi Deduction: {taxi_deduction}")
    print(f"NSSA Deduction: {nssa_deduction}")
    print(f"Net Salary: {net_salary}")
    print("------------------------")

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from fpdf import FPDF  # Added to generate PDF
    
    # Define the employee data
    data = {
        "Employee ID": ["E001", "E002", "E003", "E004"],
        "Name": ["Nicole Zonke", "Precious Tendayi", "Michael Dendera", "Millicent Gumbira"],
        "Email": ["nicolezonke@gmail.com", "precioustendayi@gmail.com", "michaeldendera@gmail.com", "millicentlisy@gmail.com"],
        "Basic Salary": [1200, 1500, 1800, 1700],
        "Allowances": [300, 400, 500, 400],
        "Taxi Deduction": [50, 60, 70, 40],
        "NSSA Deduction": [30, 40, 50, 60]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Define the email sender and recipient
    sender_email = "starlisy7@gmail.com"
    sender_password = "eoji olom dxjn duuc"
    
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
    
        # Generate a PDF for the payslip
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Payslip", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Employee ID: {employee_id}", ln=True)
        pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
        pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
        pdf.cell(200, 10, txt=f"Basic Salary: {basic_salary}", ln=True)
        pdf.cell(200, 10, txt=f"Allowances: {allowances}", ln=True)
        pdf.cell(200, 10, txt=f"Taxi Deduction: {taxi_deduction}", ln=True)
        pdf.cell(200, 10, txt=f"NSSA Deduction: {nssa_deduction}", ln=True)
        pdf.cell(200, 10, txt=f"Net Salary: {net_salary}", ln=True)
    
        # Save the PDF
        pdf_filename = f"Payslip_{employee_id}.pdf"
        pdf.output(pdf_filename)
    
        # Create a message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = f"Payslip for {name}"
    
        # Add email body
        body = f"Dear {name},\n\nPlease find attached your payslip for this month.\n\nBest regards,\nGOLDEN STAR INNOVATIONS"
        msg.attach(MIMEText(body, 'plain'))
    
        # Attach the PDF
        with open(pdf_filename, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={pdf_filename}',
            )
            msg.attach(part)
    
        # Send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())
            server.quit()
            print(f"Email sent to {email} with payslip attached.")
        except Exception as e:
            print(f"Failed to send email to {email}. Error: {e}")
    
        # Print payslip details
        print(f"Employee ID: {employee_id}")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Basic Salary: {basic_salary}")
        print(f"Allowances: {allowances}")
        print(f"Taxi Deduction: {taxi_deduction}")
        print(f"NSSA Deduction: {nssa_deduction}")
        print(f"Net Salary: {net_salary}")
        print("------------------------")
       