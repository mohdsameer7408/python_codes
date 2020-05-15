customer = {
    "name": "john  smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("name"))
print(customer.get("birth_date", "jan 1 1980"))
