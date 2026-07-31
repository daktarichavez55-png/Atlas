import os
import tkinter as tk
from tkinter import (
    filedialog,
    messagebox,
    simpledialog
)

from core.pdf_engine import (
    merge_pdfs,
    get_pdf_info,
    split_pdf
)


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
        relief="flat",
        font=("Consolas", 11)
    )
    output.pack(fill="both", expand=True, padx=20, pady=10)

    button_frame = tk.Frame(
        content,
        bg="#202124"
    )
    button_frame.pack(fill="x", padx=20, pady=10)

    def clear_output():
        output.delete("1.0", tk.END)

    # ---------------- Merge PDFs ---------------- #

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
            output.insert(
                tk.END,
                f"✓ {result}\n\n"
                f"Saved as:\n{output_file}"
            )

            messagebox.showinfo(
                "Merge Complete",
                result
            )

        except Exception as error:
            messagebox.showerror(
                "Merge Error",
                str(error)
            )

    # ---------------- PDF Info ---------------- #

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
                "==============================\n"
                "       PDF INFORMATION\n"
                "==============================\n\n"
                f"File:\n{os.path.basename(pdf_file)}\n\n"
                f"Pages:\n{info['pages']}\n\n"
                f"Encrypted:\n{'Yes' if info['encrypted'] else 'No'}"
            )

        except Exception as error:
            messagebox.showerror(
                "PDF Error",
                str(error)
            )

    # ---------------- Split PDF ---------------- #

    def split_pdf_file():

        pdf_file = filedialog.askopenfilename(
            title="Select PDF",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not pdf_file:
            return

        start_page = simpledialog.askinteger(
            "Start Page",
            "Enter the first page:"
        )

        if start_page is None:
            return

        end_page = simpledialog.askinteger(
            "End Page",
            "Enter the last page:"
        )

        if end_page is None:
            return

        output_file = filedialog.asksaveasfilename(
            title="Save Split PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not output_file:
            return

        try:

            result = split_pdf(
                pdf_file,
                output_file,
                start_page,
                end_page
            )

            output.delete("1.0", tk.END)
            output.insert(
                tk.END,
                f"✓ {result}\n\n"
                f"Saved as:\n{output_file}"
            )

            messagebox.showinfo(
                "Split Complete",
                result
            )

        except Exception as error:
            messagebox.showerror(
                "Split Error",
                str(error)
            )

    # ---------------- Buttons ---------------- #

    merge_button = tk.Button(
        button_frame,
        text="Merge PDFs",
        width=14,
        command=merge_pdf_files
    )
    merge_button.pack(side="left", padx=4)

    split_button = tk.Button(
        button_frame,
        text="Split PDF",
        width=14,
        command=split_pdf_file
    )
    split_button.pack(side="left", padx=4)

    info_button = tk.Button(
        button_frame,
        text="PDF Info",
        width=14,
        command=show_pdf_info
    )
    info_button.pack(side="left", padx=4)

    clear_button = tk.Button(
        button_frame,
        text="Clear",
        width=14,
        command=clear_output
    )
    clear_button.pack(side="left", padx=4)

    compress_button = tk.Button(
        button_frame,
        text="Compress",
        width=14,
        state="disabled"
    )
    compress_button.pack(side="left", padx=4)