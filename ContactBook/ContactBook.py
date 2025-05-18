import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and phone are required.")
        return

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    save_contacts(contacts)
    refresh_list()
    clear_entries()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def refresh_list():
    contact_list.delete(0, tk.END)
    for name in contacts:
        contact_list.insert(tk.END, f"{name} - {contacts[name]['Phone']}")

def on_select(event):
    selection = contact_list.curselection()
    if not selection:
        return
    index = selection[0]
    selected = list(contacts.items())[index]
    name, details = selected
    name_entry.delete(0, tk.END)
    name_entry.insert(0, name)
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, details["Phone"])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, details["Email"])
    address_entry.delete(0, tk.END)
    address_entry.insert(0, details["Address"])

def update_contact():
    name = name_entry.get().strip()
    if name not in contacts:
        messagebox.showerror("Update Error", "Contact not found.")
        return
    contacts[name] = {
        "Phone": phone_entry.get().strip(),
        "Email": email_entry.get().strip(),
        "Address": address_entry.get().strip()
    }
    save_contacts(contacts)
    refresh_list()
    clear_entries()

def delete_contact():
    name = name_entry.get().strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        refresh_list()
        clear_entries()
    else:
        messagebox.showerror("Delete Error", "Contact not found.")

def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone number:")
    if not query:
        return
    results = [f"{name} - {info['Phone']}" for name, info in contacts.items()
               if query.lower() in name.lower() or query in info['Phone']]
    contact_list.delete(0, tk.END)
    for result in results:
        contact_list.insert(tk.END, result)

contacts = load_contacts()

root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=1, column=1)

tk.Label(frame, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1)

tk.Label(frame, text="Address").grid(row=3, column=0)
address_entry = tk.Entry(frame, width=30)
address_entry.grid(row=3, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_contact).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Search", command=search_contact).grid(row=0, column=3, padx=5)

contact_list = tk.Listbox(root, width=50)
contact_list.pack(pady=10)
contact_list.bind('<<ListboxSelect>>', on_select)

refresh_list()
root.mainloop()
