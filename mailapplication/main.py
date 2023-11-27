import tkinter as tk
import smtplib

def send_email():
    try:
        email_address = email_entry.get()
        password = password_entry.get()
        recipient = recipient_entry.get()
        subject = subject_entry.get()
        body = body_entry.get("1.0", tk.END)
        message = "Subject: {}\n\n{}".format(subject, body)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, password)
        server.sendmail(email_address, recipient, message)
        server.quit()
        reset_fields()
        status_label.config(text="Email Sent Successfully!", fg="green")
    except Exception as e:
        status_label.config(text="Error Sending Email: {}".format(str(e)), fg="red")

def reset_fields():
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    recipient_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    body_entry.delete("1.0", tk.END)

root = tk.Tk()
root.title("Mail Application")
root.geometry("440x300")

email_label = tk.Label(root, text="Email:")
email_label.grid(row=0, column=0, padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

recipient_label = tk.Label(root, text="Recipient:")
recipient_label.grid(row=2, column=0, padx=5, pady=5)
recipient_entry = tk.Entry(root)
recipient_entry.grid(row=2, column=1, padx=5, pady=5)

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=3, column=0, padx=5, pady=5)
subject_entry = tk.Entry(root)
subject_entry.grid(row=3, column=1, padx=5, pady=5)

body_label = tk.Label(root, text="Body:")
body_label.grid(row=4, column=0, padx=5, pady=5)
body_entry = tk.Text(root, height=10, width=30)
body_entry.grid(row=4, column=1, padx=5, pady=5)

send_button = tk.Button(root, text="Send", command=send_email)
send_button.grid(row=5, column=0, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=5, column=1, padx=5, pady=5)

status_label = tk.Label(root)
status_label.grid(row=6, column=1, padx=5, pady=5)

root.mainloop()
