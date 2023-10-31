def VAT(amount):
    vat_value = (int(amount) * 0.23)

    return(f"Amount: {amount}\nVAT 23%: {vat_value}")

print(VAT(15.84))
