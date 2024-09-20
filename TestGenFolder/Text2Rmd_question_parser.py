#!/usr/bin/env python3
import re
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def parse_questions(content):
    pattern = r'```\n(Question\n========[\s\S]*?)```'
    questions = re.findall(pattern, content)
    return questions

def create_rmd_files(questions):
    # Create the "01exercises" folder if it doesn't exist
    os.makedirs("01exercises", exist_ok=True)
    
    for i, question in enumerate(questions, start=1):
        filename = os.path.join("01exercises", f"{i:02d}.rmd")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"```\n{question.strip()}\n```")
    return len(questions)

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    input_file = filedialog.askopenfilename(title="Select input file", filetypes=[("Text files", "*.txt")])
    if not input_file:
        messagebox.showerror("Error", "No input file selected.")
        return

    content = read_file(input_file)
    questions = parse_questions(content)
    total_questions = create_rmd_files(questions)
    
    messagebox.showinfo("Success", f"Total questions processed: {total_questions}\nFiles saved in 'exercises' folder.")

if __name__ == "__main__":
    main()
    # Close the console after completion
    import sys
    sys.exit()