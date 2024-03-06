import smtplib

sender_email = input("Sender Email: ")
receiver_email = input("Receiver Email: ")

subject = input("Subject: ")
message = input("Message you want to send: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender_email, "bqun tutg mxvl ixat")
server.sendmail(sender_email, receiver_email, text)
print("Email has been sent successfully")