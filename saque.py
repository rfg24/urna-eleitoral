def atm_withdrawal(amount):
    notes = [100, 50, 10, 5, 1]
    note_counts = [0, 0, 0, 0, 0]

    for i, note in enumerate(notes):
        while amount >= note:
            amount -= note
            note_counts[i] += 1

    print("Withdrawal Results:")
    for i, note in enumerate(notes):
        if note_counts[i] > 0:
            print(f"{note_counts[i]} x {note} reais")

amount = int(input("Enter the withdrawal amount (between 10 and 600 reais): "))
if 10 <= amount <= 600:
    atm_withdrawal(amount)
else:
    print("Invalid amount. Please try again.")