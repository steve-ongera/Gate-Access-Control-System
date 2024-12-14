import sqlite3
import pygame
from tkinter import *
from tkinter import messagebox, ttk

# Initialize pygame mixer for sound playback
pygame.mixer.init()

# Function to play sounds
def play_sound(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error playing sound: {e}")


# Function to handle login
def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    # Connect to the SQLite database
    conn = sqlite3.connect("tenants.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tenants WHERE username = ? AND password = ?", (username, password))
    tenant = cursor.fetchone()
    conn.close()

    if tenant:
        play_sound("access_granted.mp3")
        messagebox.showinfo("Access Granted", f"Welcome {username}!")

        if username == "steve" and password == "cp7kvt":
            open_admin_page()  # Open admin page for steve only
        else:
            refresh_login()  # Just refresh the login screen for other tenants

    else:
        play_sound("access_denied.mp3")
        messagebox.showerror("Access Denied", "Invalid username or password!")


# Admin Page
def open_admin_page():
    # Create a new window for the admin page
    root_admin = Tk()
    root_admin.title("Admin Panel")

    # Function to add tenant
    def add_tenant():
        username = username_entry.get()
        password = password_entry.get()

        if username.strip() == "" or password.strip() == "":
            messagebox.showerror("Error", "Username and Password cannot be empty!")
            return

        conn = sqlite3.connect("tenants.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tenants (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        play_sound("user-successfully-added.mp3")
        messagebox.showinfo("Success", "Tenant added successfully!")
        refresh_users()

    # Function to refresh users
    def refresh_users():
        for row in tree.get_children():
            tree.delete(row)

        conn = sqlite3.connect("tenants.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM tenants")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        conn.close()

    # Function to delete tenant
    def delete_tenant():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No tenant selected!")
            return

        tenant_id = tree.item(selected_item, "values")[0]

        conn = sqlite3.connect("tenants.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tenants WHERE id = ?", (tenant_id,))
        conn.commit()
        conn.close()

        play_sound("delete-successful.mp3")
        messagebox.showinfo("Success", "Tenant deleted successfully!")
        refresh_users()

    # Function to update tenant
    def update_tenant():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No tenant selected!")
            return

        tenant_id = tree.item(selected_item, "values")[0]
        new_username = username_entry.get()
        new_password = password_entry.get()

        if new_username.strip() == "" or new_password.strip() == "":
            messagebox.showerror("Error", "Username and Password cannot be empty!")
            return

        conn = sqlite3.connect("tenants.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE tenants SET username = ?, password = ? WHERE id = ?", (new_username, new_password, tenant_id))
        conn.commit()
        conn.close()

        play_sound("update-successful.mp3")
        messagebox.showinfo("Success", "Tenant updated successfully!")
        refresh_users()

    # Admin Page Layout
    admin_frame = LabelFrame(root_admin, text="Admin Panel", padx=10, pady=10)
    admin_frame.pack(padx=10, pady=10)

    username_label = Label(admin_frame, text="Username:")
    username_label.grid(row=0, column=0)
    username_entry = Entry(admin_frame)
    username_entry.grid(row=0, column=1)

    password_label = Label(admin_frame, text="Password:")
    password_label.grid(row=1, column=0)
    password_entry = Entry(admin_frame, show="*")
    password_entry.grid(row=1, column=1)

    add_tenant_button = Button(admin_frame, text="Add Tenant", command=add_tenant)
    add_tenant_button.grid(row=2, column=0)

    update_tenant_button = Button(admin_frame, text="Update Tenant", command=update_tenant)
    update_tenant_button.grid(row=2, column=1)

    delete_tenant_button = Button(admin_frame, text="Delete Tenant", command=delete_tenant)
    delete_tenant_button.grid(row=2, column=2)

    tree = ttk.Treeview(admin_frame, columns=("ID", "Username"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Username", text="Username")
    tree.grid(row=3, column=0, columnspan=3)

    refresh_users()  # Load initial data
    root_admin.mainloop()


# Function to refresh the login page
def refresh_login():
    login_username_entry.delete(0, END)
    login_password_entry.delete(0, END)


# Login Page
root_login = Tk()
root_login.title("Login Page")

login_frame = LabelFrame(root_login, text="Login", padx=10, pady=10)
login_frame.pack(padx=10, pady=10)

login_username_label = Label(login_frame, text="Username:")
login_username_label.grid(row=0, column=0)
login_username_entry = Entry(login_frame)
login_username_entry.grid(row=0, column=1)

login_password_label = Label(login_frame, text="Password:")
login_password_label.grid(row=1, column=0)
login_password_entry = Entry(login_frame, show="*")
login_password_entry.grid(row=1, column=1)

login_button = Button(login_frame, text="Login", command=login)
login_button.grid(row=2, columnspan=2)

root_login.mainloop()
