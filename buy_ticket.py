import tkinter as tk

tickets_info = {
    1: [
        {"уақыт": "10:00", "бағасы": " 5000 тг"},
        {"уақыт": "12:00", "бағасы": "7000 тг"},
        {"уақыт": "15:00", "бағасы": "8000 тг"},
    ],
    2: [
        {"уақыт": "08:00", "бағасы": "30000 тг"},
        {"уақыт": "11:00", "бағасы": "25000 тг"},
        {"уақыт": "14:00", "бағасы": "15000 тг"},
    ],
    3: [
        {"уақыт": "09:30", "бағасы": "2000 тг"},
        {"уақыт": "13:00", "бағасы": "3000 тг"},
        {"уақыт": "16:00", "бағасы": "1500 тг"},
    ]
}

# Глобальные переменные для хранения информации о купленных и возвращенных билетах
purchased_tickets = {1: 0, 2: 0, 3: 0}
returned_tickets = {1: 0, 2: 0, 3: 0}


def show_tickets():
    transport = var.get()
    ticket_info.config(state=tk.NORMAL)
    ticket_info.delete(1.0, tk.END)

    if transport in tickets_info:
        tickets = tickets_info[transport]
        for ticket in tickets:
            ticket_info.insert(tk.END, f"Уақыт: {ticket['уақыт']}, Бағасы: {ticket['бағасы']}\n")

        # Вывод информации о количестве купленных и возвращенных билетов
        ticket_info.insert(tk.END, f"\nСатып алған билеттер саны: {purchased_tickets[transport]}\n")
        ticket_info.insert(tk.END, f"Қайтарылды билеттер саны: {returned_tickets[transport]}\n")
    else:
        ticket_info.insert(tk.END, "Билеттер туралы ақпарат жоқ")

    ticket_info.config(state=tk.DISABLED)


def buy_tickets():
    transport = var.get()
    quantity = int(quantity_entry.get())

    # Здесь можно добавить логику для покупки указанного количества билетов
    purchased_tickets[transport] += quantity
    show_tickets()


def refund_tickets():
    transport = var.get()
    quantity = int(quantity_entry.get())

    # Здесь можно добавить логику для возврата указанного количества билетов за деньги
    returned_tickets[transport] += quantity
    show_tickets()


root = tk.Tk()
root.title("Тасымалдар билеттері")

var = tk.IntVar()

tk.Radiobutton(root, text="Поезд", variable=var, value=1, command=show_tickets).pack()
tk.Radiobutton(root, text="Ұшақ", variable=var, value=2, command=show_tickets).pack()
tk.Radiobutton(root, text="Автобус", variable=var, value=3, command=show_tickets).pack()

ticket_info = tk.Text(root, height=10, width=30)
ticket_info.pack()

show_tickets_button = tk.Button(root, text="Билеттерді көрсету", command=show_tickets)
show_tickets_button.pack()

quantity_label = tk.Label(root, text="Көрсетілген билет саны:")
quantity_label.pack()

quantity_entry = tk.Entry(root)
quantity_entry.pack()

buy_tickets_button = tk.Button(root, text="Билеттерді сатып алу", command=buy_tickets)
buy_tickets_button.pack()

refund_tickets_button = tk.Button(root, text="Билеттерді қайтару ", command=refund_tickets)
refund_tickets_button.pack()

ticket_info.config(state=tk.DISABLED)

root.mainloop()
