import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to predict the study program based on the highest score
def predict_study_program():
    # Get values from entry widgets
    nama_siswa = entry_nama.get()
    nilai_biologi = int(entry_biologi.get())
    nilai_fisika = int(entry_fisika.get())
    nilai_inggris = int(entry_inggris.get())

    # Determine the predicted study program based on the highest score
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi_fakultas = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi_fakultas = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi_fakultas = "Bahasa"
    else:
        prediksi_fakultas = "Tidak dapat diprediksi"

    # Display the predicted study program
    result_text = f"Predicted study program for {nama_siswa}: {prediksi_fakultas}"
    output_label.config(text=result_text)

    # Save data to SQLite database
    save_to_database(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas)

# Function to save data to SQLite database
def save_to_database(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas):
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')

    # Insert data into the table
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Create the main window
root = tk.Tk()
root.title("Study Program Prediction Application")
root.geometry("400x300")  # Set the window size

# Create and configure entry widgets
entry_nama = tk.Entry(root, width=30, justify='center')
entry_nama_label = tk.Label(root, text="Nama Siswa:")
entry_nama_label.pack(pady=5)
entry_nama.pack()

entry_biologi = tk.Entry(root, width=30, justify='center')
entry_biologi_label = tk.Label(root, text="Nilai Biologi:")
entry_biologi_label.pack(pady=5)
entry_biologi.pack()

entry_fisika = tk.Entry(root, width=30, justify='center')
entry_fisika_label = tk.Label(root, text="Nilai Fisika:")
entry_fisika_label.pack(pady=5)
entry_fisika.pack()

entry_inggris = tk.Entry(root, width=30, justify='center')
entry_inggris_label = tk.Label(root, text="Nilai Inggris:")
entry_inggris_label.pack(pady=5)
entry_inggris.pack()

# Create the "Submit" button
submit_button = tk.Button(root, text="Submit", command=predict_study_program)
submit_button.pack(pady=10)

# Create the production output label
output_label = tk.Label(root, text="", font=("Helvetica", 12))
output_label.pack()

root.mainloop()
