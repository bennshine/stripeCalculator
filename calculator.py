# -*- coding: latin-1 -*-
def calculate_total_charge(net_payment, stripe_flat_fee, stripe_percentage_fee, xerata_percentage_fee):
    # Calculate the Stripe fee
    stripe_fee = (stripe_percentage_fee / 100) * net_payment + stripe_flat_fee

    # Calculate the Xerata fee
    xerata_fee = (xerata_percentage_fee / 100) * net_payment

    # Calculate the total charge amount
    total_charge = net_payment + stripe_fee + xerata_fee
    return total_charge

try:
    # Input your desired net payment (e.g., 100)
    net_payment = float(input("Enter the desired net payment: "))

    # Replace with your actual Stripe flat fee and percentage fee
    stripe_flat_fee = 0.25
    stripe_percentage_fee = 1.5

    # Replace with your custom percentage fee
    xerata_percentage_fee = 0.047

    # Calculate the total charge
    total_charge = calculate_total_charge(net_payment, stripe_flat_fee, stripe_percentage_fee, xerata_percentage_fee)
    print(f"Total charge amount: €{total_charge:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numeric value.")