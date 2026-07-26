import tkinter as tk

root = tk.Tk()

root.title("Atlas")
root.geometry("900x600")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="ATLAS",
    font=("Segoe UI", 28, "bold"),
    fg="white",
    bg="#1e1e1e"
)

subtitle = tk.Label(
    root,
    text="Version 0.0.1",
    font=("Segoe UI", 12),
    fg="#bbbbbb",
    bg="#1e1e1e"
)

title.pack(pady=80)
subtitle.pack()

root.mainloop()