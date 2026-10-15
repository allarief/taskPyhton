
import tkinter as tk
from tkinter import messagebox


def calculate_discount():
    try:
        original_price = float(price_entry.get())
        discount_rate = float(discount_entry.get())
        quantity = int(quantity_entry.get())

        if original_price < 0:
            raise ValueError("Price cannot be negative.")

        if not 0 <= discount_rate <= 100:
            raise ValueError("Discount must be between 0 and 100.")

        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        subtotal = original_price * quantity
        discount_amount = subtotal * discount_rate / 100
        final_price = subtotal - discount_amount

        result_label.config(
            text=(
                f"Subtotal: Rp {subtotal:,.2f}\n"
                f"Discount: Rp {discount_amount:,.2f}\n"
                f"Final Price: Rp {final_price:,.2f}"
            )
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers.\n"
            "Discount must be 0–100 and quantity at least 1."
        )


def clear_fields():
    price_entry.delete(0, tk.END)
    discount_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    quantity_entry.insert(0, "1")
    result_label.config(text="Final Price: Rp 0.00")


# Main window
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("420x400")
root.resizable(False, False)

# Heading
title_label = tk.Label(
    root,
    text="Discount Calculator",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

# Original price
tk.Label(root, text="Original Price (Rp)").pack()
price_entry = tk.Entry(root, justify="center")
price_entry.pack(pady=5)

# Discount percentage
tk.Label(root, text="Discount (%)").pack()
discount_entry = tk.Entry(root, justify="center")
discount_entry.pack(pady=5)

# Quantity
tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root, justify="center")
quantity_entry.insert(0, "1")
quantity_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=12)

tk.Button(
    button_frame,
    text="Calculate",
    command=calculate_discount,
    width=12
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    width=12
).pack(side="left", padx=5)

# Result
result_label = tk.Label(
    root,
    text="Final Price: Rp 0.00",
    font=("Arial", 11, "bold"),
    justify="center"
)
result_label.pack(pady=8)

root.mainloop()
