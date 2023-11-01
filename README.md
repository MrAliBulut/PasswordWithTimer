# Random Password Generator and Emailer

This Python script generates a random 6-digit password, emails it to a provided address, and allows the user to verify the password within a limited time frame.

## Functions

1. **`generate_random_password()`**
   - Generates a random 6-digit password.

2. **`send_password_to_email(password, email)`**
   - Sends the generated password to the provided email address using an Outlook account.

3. **`password_control(email, generated_password)`**
   - Controls the validity of the entered password within a 2-minute time frame.

4. **`main()`**
   - Executes the main functionality of the script.
   
## Usage

1. Run the script (`python password_generator.py`).
2. Enter your email address when prompted.
3. A random 6-digit password will be generated and sent to the provided email address. Please check your spam folder if necessary.
4. Follow the prompts to enter the received password within the given time frame.

## Note

- The password is set to expire after 2 minutes.

## Requirements

- Python 3.x
- `smtplib` module (for email functionality)

## Special Thanks

Special thanks to ChatGPT for assistance in refining the README and the code itself. 
Your contributions were invaluable!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This means this is an open source code. Please feel free to use it however you please. You can modify, distribute, and even use it for commercial purposes. If you do use it, a link back to this repository would be appreciated, but is not required.

---
