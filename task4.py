data = [
 {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
 {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
 {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
 {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
 {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
 {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
]

workers = {sale ["name"] for sale in data}

money = {name: sum(sale["price"] for sale in data if sale
["name"] == name ) for name in workers}

print("Множина працівників: ", workers)

print("Словник ")
for name, full_money in money.items():
    print(f"{name}: {full_money}")