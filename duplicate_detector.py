import tkinter as tk
from tkinter import scrolledtext, simpledialog

def label_duplicates(event=None):
    input_text = text_original.get("1.0", tk.END)  # Get all text from the original text box
    lines = input_text.strip().splitlines()  # Split into lines
    unique_lines = []
    duplicates = []
    line_count = {}

    # Count occurrences of each line
    for line in lines:
        if line in line_count:
            line_count[line] += 1
            duplicates.append(line)  # Collect duplicates
        else:
            line_count[line] = 1
            unique_lines.append(line)  # Keep unique lines

    # Ask user for a custom label for duplicates if not already done
    if not hasattr(label_duplicates, "duplicate_label"):
        label_duplicates.duplicate_label = simpledialog.askstring("Custom Label", "Enter label for duplicates (default: [DUPLICATE]):")
        if not label_duplicates.duplicate_label:  # If no input, use the default label
            label_duplicates.duplicate_label = "[DUPLICATE]"

    # Clear previous duplicates
    text_duplicates.delete("1.0", tk.END)

    # Display labeled duplicate lines in the duplicates text box
    if duplicates:
        labeled_duplicates = [f"{label_duplicates.duplicate_label} {line}" for line in set(duplicates)]
        text_duplicates.insert(tk.END, "\n".join(labeled_duplicates))
    else:
        text_duplicates.insert(tk.END, "No duplicates found.")

    # Update original text area to show only unique lines
    text_original.delete("1.0", tk.END)
    text_original.insert(tk.END, "\n".join(unique_lines))

    # Update line counts
    original_count_label.config(text=f"Original Line Count: {len(unique_lines)}")
    duplicate_count_label.config(text=f"Found Duplicate Line Count: {len(set(duplicates))}")

def remove_duplicates():
    # Get the current text from the duplicates box and remove it from the original text
    duplicates_text = text_duplicates.get("1.0", tk.END).strip()  # Get all text from duplicates box
    duplicates_lines = duplicates_text.splitlines()

    # Get current text from original text box
    original_text = text_original.get("1.0", tk.END).strip()
    original_lines = original_text.splitlines()

    # Remove duplicates from the original lines
    new_original_lines = [line for line in original_lines if line not in duplicates_lines]

    # Update the original text box
    text_original.delete("1.0", tk.END)
    text_original.insert(tk.END, "\n".join(new_original_lines))

    # Update the original line count
    original_count_label.config(text=f"Original Line Count: {len(new_original_lines)}")

def clear_text():
    text_original.delete("1.0", tk.END)  # Clear original text area
    text_duplicates.delete("1.0", tk.END)  # Clear duplicates text area
    original_count_label.config(text="Original Line Count: 0")  # Reset original line count
    duplicate_count_label.config(text="Found Duplicate Line Count: 0")  # Reset duplicate line count

# Set up the main application window
app = tk.Tk()
app.title("Duplicate Line Detector")

# Original Text Area
label_original = tk.Label(app, text="Original Text:")
label_original.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))  # Add some padding above
text_original = scrolledtext.ScrolledText(app, wrap=tk.WORD)
text_original.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

# Duplicates Text Area
label_duplicates = tk.Label(app, text="Found Duplicates:")
label_duplicates.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))  # Add some padding above
text_duplicates = scrolledtext.ScrolledText(app, wrap=tk.WORD)
text_duplicates.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

# Line Count Labels
original_count_label = tk.Label(app, text="Original Line Count: 0")
original_count_label.grid(row=4, column=0, sticky="w", padx=10, pady=(5, 0))

duplicate_count_label = tk.Label(app, text="Found Duplicate Line Count: 0")
duplicate_count_label.grid(row=5, column=0, sticky="w", padx=10, pady=(5, 0))

# Buttons Frame
button_frame = tk.Frame(app)
button_frame.grid(row=6, column=0, pady=10)

# Remove Duplicates Button
remove_button = tk.Button(button_frame, text="Remove Duplicates from Original", command=remove_duplicates)
remove_button.pack(side=tk.LEFT, padx=5)

# Clear Button
clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)

# Bind the original text area to the label_duplicates function
text_original.bind("<KeyRelease>", label_duplicates)

# Configure grid to make the text areas expand with window resizing
app.grid_rowconfigure(1, weight=1)  # Allow the original text area to expand
app.grid_rowconfigure(3, weight=1)  # Allow the duplicates text area to expand
app.grid_columnconfigure(0, weight=1)  # Allow the column to expand

# Start the GUI event loop
app.mainloop()
