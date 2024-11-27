import smtplib
import random
import getpass

def secret_santa(names_emails, couples):
    """
    Organizes a Secret Santa drawing and sends emails to participants,
    preventing spouses from being assigned to each other.

    Args:
        names_emails (dict): A dictionary of participant names and emails.
        couples (list): A list of tuples, each containing the names of a couple.
    """
    names = list(names_emails.keys())
    random.shuffle(names)

    # # Ensure no one gets assigned to themselves or their spouse
    # while any(names[i] == names[(i + 1) % len(names)] for i in range(len(names))):
    #     random.shuffle(names)

    # Ensure no one gets assigned to themselves... or their spouse
    valid = False
    while not valid:
        valid = True
        for i in range(len(names)):
            sender = names[i]
            recipient = names[(i + 1) % len(names)]  # handles the wrap-around case
            if sender == recipient or ((sender, recipient) in couples or (recipient, sender) in couples):
                valid = False
                random.shuffle(names)
                break  # Reshuffle and restart checks

    # Get sender email and password
    sender_email = input("Enter your email address: ")
    sender_password = getpass.getpass("Enter your App password: ")
    # note: You need to create an (16 character) App password on your gmail account and use this as your password.
    # You can delete that App password later

    # Send emails
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        for i in range(len(names)):
            sender = names[i]
            recipient = names[(i + 1) % len(names)]
            email_subject = "Amigo Secreto Asignado !"
            if recipient == "David":
                email_body = f"Jo jo jo! Eres el amigo secreto de (su merce') EL (Don Carlos) {recipient} !"
            else:
                email_body = f"Jo jo jo! Eres el amigo secreto de {recipient} !"

            message = f"Subject: {email_subject}\n\n{email_body}"
            server.sendmail(sender_email, names_emails[sender], message)


participants = {
    "Alice": "alice@gmail.com",
    "Bob": "bob@email.com",
    "Charlie": "charlie@email.com",
    "David": "david@email.com",
    "Emily": "emily@email.com",
}

couples = [("Alice", "Bob"),
           ("David", "Emily"),
           ]  # Define couples to prevent them from gifting each other

secret_santa(participants, couples)
