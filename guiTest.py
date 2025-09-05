import tkinter as tk
import subprocess
import shlex

# This function is called when the button is clicked.
def run_other_script():
    # Get the text from the entry field.
    input_text = entry_field.get()
    
    # Check if the text box is empty
    if not input_text:
        print("Error: The text box is empty.")
        return
    
    # Use subprocess.run() to execute the other script.
    # We pass the input_text as a command-line argument.
    # shlex.quote() is used to properly handle spaces and special characters.
    try:
        # Pass the input_text as an argument to other_script.py
        subprocess.run(['python', 'other_script.py', shlex.quote(input_text)])
    except FileNotFoundError:
        print("Error: 'other_script.py' not found.")

def close_app():
    root.destroy()


# Create the main window
root = tk.Tk()
root.title("Main GUI")
root.geometry("900x300")

# Create a label to instruct the user
label = tk.Label(root, text="Enter a value to pass to the other script:")
label.pack(pady=10)

entry_field = tk.Entry(root, width=50)
entry_field.pack(pady=5)

# Create a button that calls the run_other_script function
my_button = tk.Button(root, text="Generate Song", command=run_other_script)
my_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=close_app)
exit_button.pack(pady=10)

root.mainloop()
