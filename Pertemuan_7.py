import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# Create SQLite connection and cursor
conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

# Create table if not exists
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
conn.commit()

matkul = tk.Tk()

matkul.configure(background="Green")
matkul.geometry("600x600")
matkul.title("Pertemuan 7")

title_label = ttk.Label(matkul, text="Prediksi Fakultas Kamu", font=("Times New Roman", 16))
title_label.pack(pady=20)

nama_siswa_label = ttk.Label(matkul, text="Nama Siswa:")
nama_siswa_label.pack(pady=5)
nama_siswa_entry = ttk.Entry(matkul)
nama_siswa_entry.pack(pady=5)

subject_labels = []
subject_entries = []

for subject in ["Biologi", "Fisika", "Inggris"]:
    subject_label = ttk.Label(matkul, text=f"Nilai {subject}:")
    subject_label.pack(pady=5)

    subject_entry = ttk.Entry(matkul)
    subject_entry.pack(pady=5)

    subject_labels.append(subject_label)
    subject_entries.append(subject_entry)

def Prodi_Kamu():

    nama_siswa = nama_siswa_entry.get()
    nilai_biologi = int(subject_entries[0].get())
    nilai_fisika = int(subject_entries[1].get())
    nilai_inggris = int(subject_entries[2].get())

    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi_fakultas = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi_fakultas = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi_fakultas = "Bahasa"
    else:
        prediksi_fakultas = "Belum dapat diprediksi"

    output_text = f"Fakultas kamu adalah: {prediksi_fakultas}"
    output_label.config(text=output_text)
    messagebox.showinfo("Hasil prediksi kamu", output_text)

    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas))
    conn.commit()

# membuat button
button = ttk.Button(matkul, text="Submit", command=Prodi_Kamu)
button.pack(pady=15)

# membuat label
output_label = ttk.Label(matkul, text="", font=("Times New Roman", 14))
output_label.pack()

matkul.mainloop()

# Close the SQLite connection
conn.close()
