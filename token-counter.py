#!/bin/env python3
import tiktoken


def encode(text, encoding="cl100k_base"):
    enc = tiktoken.get_encoding(encoding)
    for x in enc.encode(text):
        yield x


def main():
    import tkinter as tk
    root = tk.Tk()
    root.geometry("800x600")
    root.title("A simple Tiktoken token GUI counter")

    # Add instructions label above the text entry box
    instructions_label = tk.Label(
            root, text="Paste or insert your text below to count tokens:")
    instructions_label.grid(row=0, column=0, sticky="w", padx=5, pady=2)

    # Create the Text widget for multiline input
    entry_text = tk.Text(root)
    entry_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    # Configure the grid to allow the Text widget to resize with the window
    root.grid_rowconfigure(1, weight=1)  # Makes the row with the Text widget grow
    root.grid_columnconfigure(0, weight=1)  # Makes the column with the Text widget grow

    def count():
        text = entry_text.get("1.0", "end-1c")  # Get the text from the Text widget
        tokens = list(encode(text))
        result.config(text=f"number of tokens: {len(tokens)}")
    result = tk.Label(root, text="number of tokens:")
    result.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    tk.Button(root, text="Count", command=count).grid(row=3, column=0)
    root.mainloop()


if __name__ == "__main__":
    main()
