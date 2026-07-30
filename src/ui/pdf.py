import tkinter as tk
from tkinter import filedialog, messagebox

from core.pdf_engine import merge_pdfs, get_pdf_info


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

    def merge_pdf_files():

        pdf_files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not pdf_files:
            return

        output_file = filedialog.asksaveasfilename(
            title="Save merged PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not output_file:
            return

        try:
            result = merge_pdfs(pdf_files, output_file)

            output.delete("1.0", tk.END)
            output.insert(tk.END, result)

            messagebox.showinfo(
                "Success",
                "PDFs merged successfully!"
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def show_pdf_info():

        pdf_file = filedialog.askopenfilename(
            title="Select PDF",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not pdf_file:
            return

        try:
            info = get_pdf_info(pdf_file)

            output.delete("1.0", tk.END)
            output.insert(
                tk.END,
                f"File: {pdf_file}\n\n"
                f"Pages: {info['pages']}\n"
                f"Encrypted: {info['encrypted']}"
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    merge_button = tk.Button(
        button_frame,
        text="Merge PDFs",
        width=15,
        command=merge_pdf_files
    )
    merge_button.pack(side="left", padx=5)

    split_button = tk.Button(
        button_frame,
        text="Split PDF",
        width=15
    )
    split_button.pack(side="left", padx=5)

    info_button = tk.Button(
        button_frame,
        text="PDF Info",
        width=15,
        command=show_pdf_info
    )
    info_button.pack(side="left", padx=5)

    compress_button = tk.Button(
        button_frame,
        text="Compress",
        width=15
    )
    compress_button.pack(side="left", padx=5)