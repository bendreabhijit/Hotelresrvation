import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def load_email_template():
    # Get the absolute path to the current working directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Build the full path to the email template
    template_path = os.path.join(current_directory, 'email_template.html')
    
    with open(template_path, 'r') as f:
        template = f.read()
    return template

def send_booking_email(to_email, customer_name, booking_id, room_name, check_in_date, check_out_date):
    # Your SMTP server credentials (use your actual details)
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = "hoteloberoibooking@gmail.com" #os.getenv("SMTP_USERNAME")
    smtp_password = "lifu eays obar fqjn"#os.getenv("SMTP_PASSWORD")  # Use App Password if 2FA is enabled

    # Load the email template

    print(to_email, customer_name, booking_id, room_name, check_in_date, check_out_date)

    email_content = load_email_template()
 
    email_content = email_content.replace('{{customer_name}}', customer_name)
    email_content = email_content.replace('{{booking_id}}', str(booking_id))
    email_content = email_content.replace('{{room_name}}', str("delux"))
    email_content = email_content.replace('{{room_id}}', str(room_name))
    email_content = email_content.replace('{{check_in_date}}', str(check_in_date))
    email_content = email_content.replace('{{check_out_date}}', str(check_out_date))

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = 'Your Room Booking Confirmation'
    msg.attach(MIMEText(email_content, 'html'))

    # Connect to the server
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    
    # Send email
    server.sendmail(smtp_username, to_email, msg.as_string())

    # Close connection
    server.quit()

   
# Example usage
