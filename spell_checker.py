import tkinter as tk
from tkinter import messagebox
from spellchecker import SpellChecker

# Initialize the spell checker
spell = SpellChecker()

def check_spelling(input_text):
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    # Split the text into words and find misspelled ones
    words = input_text.split()
    misspelled = spell.unknown(words)

    if not misspelled:
        messagebox.showinfo("No Errors", "No spelling errors found!")
        return
    # Suggest corrections for each misspelled word
    corrections = {word: spell.correction(word) for word in misspelled}
    # Display the corrections in the output text widget
    output_text.delete(1.0, tk.END)  # Clear previous output
    for word, correction in corrections.items():
        output_text.insert(tk.END, f"{word} -> {correction}\n")
def clear_text():
    input_text.delete(1.0, tk.END)
    output_text.delete(1.0, tk.END)
# Create the GUI window
root = tk.Tk()
root.title("Spell Checker")
# Set background color and window size
root.configure(bg="lightblue")
root.geometry("700x600")
# Heading Label
heading_label = tk.Label(root, text="Spell Checker", font=("Helvetica", 30, "bold"), fg="darkblue", bg="lightblue", pady=10)
heading_label.pack(pady=20)
# Input label
input_label = tk.Label(root, text="Enter Text:", font=("Helvetica", 14), fg="black", bg="lightblue")
input_label.pack(pady=5)
# Text box for user input with styling
input_text = tk.Text(root, width=80, height=10, font=("Arial", 16), bg="white", fg="black", wrap=tk.WORD, bd=2, relief="solid", padx=10, pady=10)
input_text.pack(pady=10)
# Button frame to hold "Check Spelling" and "Clear" buttons side by side
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)
# Button to check spelling with styling (Text color set to black)
check_button = tk.Button(button_frame, text="Check Spelling", font=("Arial", 14), fg="black", bg="green", command=lambda: check_spelling(input_text.get("1.0", tk.END)), relief="raised", width=15)
check_button.grid(row=0, column=0, padx=10)
# Clear button to reset both input and output text fields with styling (Text color set to black)
clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 14), fg="black", bg="red", command=clear_text, relief="raised", width=15)
clear_button.grid(row=0, column=1, padx=10)
# Output label
output_label = tk.Label(root, text="Corrections:", font=("Helvetica", 14), fg="black", bg="lightblue")
output_label.pack(pady=5)
# Text box for displaying results with styling
output_text = tk.Text(root, width=80, height=10, font=("Arial", 16), bg="white", fg="black", wrap=tk.WORD, bd=2, relief="solid", padx=10, pady=10)
output_text.pack(pady=10)
# Start the Tkinter main loop
root.mainloop()

