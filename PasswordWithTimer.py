import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

def generate_random_password():
    return ''.join(random.choices('0123456789', k=6))

def send_password_to_email(password, email):
    
    # Outlook account information
    sender_email = "PasswordSender_al@outlook.com"  # Sender email address
    sender_password = "password_al_sender"        # Sender email password
    #I've created a new email address to send the password.
    
    # Email subject and content
    subject = "Password Request"
    body = f"Your password: {password}"
    
    # Creating and sending the email
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = email
    
    try:
        # Connecting to the Outlook SMTP server. Gmail gives us an error.
        server = smtplib.SMTP("smtp.office365.com", 587)  # Outlook address and port  
        
        # Opening the server connection
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Sending the email
        server.sendmail(sender_email, [email], msg.as_string())
        print(f"\n\nYour Password has been sent to: {email}. \nPlease don't forget to check your spam folder .")

        # Closing the server connection
        server.quit()

    except Exception as e:
        print(f"\n\nWe came across an error while sending the e-mail, Error: {e}")

def password_control(email, generated_password):

    expiry = datetime.now() + timedelta(seconds=120)  # Password expiration time (2 minutes)

    while datetime.now() < expiry:

        user_input = input("\n\nPlease enter your password: ")
        
        if user_input == generated_password: 

            if datetime.now() > expiry:
                print("\nYour password has expired")
                return False
            
            else:

                print("\nYou have entered your password successfully and in time")
                return True
            
        else:
            print("\nIncorrect password, please try again.")
    
    print("\nYour password is no longer valid.")




def main():
    email = input("E-mail Adress: ")
    generated_password = generate_random_password()
    send_password_to_email(generated_password, email)
    
    if not password_control(email, generated_password):
        return
    

if __name__ == "__main__":
    main()
