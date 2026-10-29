
import tkinter as tk
from tkinter import messagebox, filedialog
import pyttsx3
import threading

# Create the speech engine
engine = pyttsx3.init()

# Function to speak the text
def speak_text():
    text = text_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return

    def speak():
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=speak, daemon=True).start()


# Function to stop speaking
def stop_speech():
    engine.stop()


# Function to save speech as an audio file
def save_audio():
    text = text_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("MP3 Audio", "*.mp3"), ("WAV Audio", "*.wav")]
    )

    if file_path:
        try:
            engine.save_to_file(text, file_path)
            engine.runAndWait()
            messagebox.showinfo("Success", "Audio saved successfully!")
        except Exception as error:
            messagebox.showerror("Error", str(error))


# Function to clear the text
def clear_text():
    text_box.delete("1.0", tk.END)


# Create the main window
root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("600x450")
root.configure(bg="#eaf2f8")

# Heading
heading = tk.Label(
    root,
    text="Text-to-Speech Converter",
    font=("Arial", 20, "bold"),
    bg="#eaf2f8",
    fg="#1a5276"
)
heading.pack(pady=15)

# Instruction
instruction = tk.Label(
    root,
    text="Enter your text below:",
    font=("Arial", 12),
    bg="#eaf2f8"
)
instruction.pack()

# Text input box
text_box = tk.Text(root, height=10, width=60, font=("Arial", 11))
text_box.pack(pady=10, padx=15)

# Buttons
button_frame = tk.Frame(root, bg="#eaf2f8")
button_frame.pack(pady=10)

tk.Button(
    button_frame, text="Speak",
    command=speak_text, width=12, bg="#2e86c1", fg="white"
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame, text="Stop",
    command=stop_speech, width=12
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame, text="Save Audio",
    command=save_audio, width=12
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame, text="Clear",
    command=clear_text, width=12
).grid(row=0, column=3, padx=5)

# Run the application
root.mainloop()
