import smtplib

def test_smtp_connection(smtp_server, smtp_port, smtp_username, smtp_password):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure if using TLS
        server.login(smtp_username, smtp_password)
        print("SMTP connection successful!")
        server.quit()
    except Exception as e:
        print("SMTP connection failed:", e)

# Replace with your credentials and settings
test_smtp_connection("smtp.gmail.com", 587, "hoteloberoibooking@gmail.com", "lifu eays obar fqjn")
