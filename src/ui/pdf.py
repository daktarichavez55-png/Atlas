import tkinter as tk


def show_pdf(content):

    # Clear current page
    for widget in content.winfo_children():
        widget.destroy()

    title = tk.Label(
        content,
        text="PDF Tools",
        font=("Segoe UI", 24, "bold"),
        bg="#202124",
        fg="white"
    )
    title.pack(pady=(30, 15))

    output = tk.Text(
        content,
        height=15,
        bg="#2b2d31",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    output.pack(fill="both", expand=True, padx=20, pady=10)

    button_frame = tk.Frame(
        content,
        bg="#202124"
    )
    button_frame.pack(fill="x", padx=20, pady=10)

    merge_button = tk.Button(
        button_frame,
        text="Merge PDFs",
        width=15
    )
    merge_button.pack(side="left", padx=5)

    split_button = tk.Button(
        button_frame,
        text="Split PDF",
        width=15
    )
    split_button.pack(side="left", padx=5)

    compress_button = tk.Button(
        button_frame,
        text="Compress",
        width=15
    )
    compress_button.pack(side="left", padx=5)