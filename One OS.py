import tkinter as tk
import subprocess

def process_command():
    command = entry.get()
    output_text.insert(tk.END, f"> {command}\n")

    if command == "help":
        output_text.insert(tk.END, "Available commands:\n")
        output_text.insert(tk.END, "- help: Display available commands\n")
        output_text.insert(tk.END, "- version: Show the current version\n")
        output_text.insert(tk.END, "- open <file>: Open a file\n")
        output_text.insert(tk.END, "- save <file>: Save a file\n")
        output_text.insert(tk.END, "- run <script.py>: Run another Python script\n")
        output_text.insert(tk.END, "- exit: Exit the program\n")
    elif command == "version":
        output_text.insert(tk.END, "One OS Version 1.0\n")
    elif command.startswith("open"):
        filename = command.split(" ")[1]
        output_text.insert(tk.END, f"Opening file: {filename}\n")
        # Logic to open the specified file
    elif command.startswith("save"):
        filename = command.split(" ")[1]
        output_text.insert(tk.END, f"Saving file: {filename}\n")
        # Logic to save the specified file
    elif command.startswith("run"):
        script_name = command.split(" ")[1]
        if script_name == "web_browser.py":
            output_text.insert(tk.END, f"Running script: {script_name}\n")
            try:
                subprocess.run(["python", script_name])
            except FileNotFoundError:
                output_text.insert(tk.END, f"Error: File '{script_name}' not found\n")
        
    elif command == "start_system":
        output_text.insert(tk.END, "Starting UI for system")
    else:
        output_text.insert(tk.END, "Invalid command. Type 'help' for available commands.\n")

    # Clear the entry field
    entry.delete(0, tk.END)

window = tk.Tk()
window.title('One OS')
window.geometry("550x370")
window.configure(bg='black')
output_text = tk.Text(window, height=20, width=60,fg='white',bg='black')
output_text.pack()

entry = tk.Entry(window, width=60)
entry.pack()

initial_text = "One OS Alpha 1.0"  # Initial text for the command
output_text.insert(tk.END, f"> {initial_text}\n")  # Fill the initial text in the output area

submit_button = tk.Button(window, text="Submit", command=process_command)
submit_button.pack()

window.mainloop()
