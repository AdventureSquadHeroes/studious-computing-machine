import smtplib

class Contact:

    def __init__(self, name, email, body, subject=None):
        self.name = name
        self.email = email
        self.subject = subject
        self.body = body


    def send_message(self):
        with smtplib.SMTP("email") as connection:
            connection.starttls()
            connection.login(user="", password="")
            connection.sendmail(
                from_addr="",
                to_addrs="",
                msg=f"{self.subject}\n\n{self.name}\n{self.email}\n{self.body}"
            )