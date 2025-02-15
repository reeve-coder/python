items_in_shop = [
    {
        "name": "Peanuts         ",
        "id": 1,
        "cost": 50
    },
    {
        "name": "Chakli          ",
        "id": 2,
        "cost": 30
    },
    {
        "name": "Poha            ",
        "id": 3,
        "cost": 40
    },
    {
        "name": "Shev            ",
        "id": 4,
        "cost": 20
    },
    {
        "name": "French Vanilla  ",
        "id": 5,
        "cost": 60
    },
    {
        "name": "Hot Chocolate   ",
        "id": 6,
        "cost": 15
    },
    {
        "name": "Sabudana        ",
        "id": 7,
        "cost": 35
    },
    {
        "name": "Triangular Chips",
        "id": 8,
        "cost": 25
    },
    {
        "name": "Kurmure         ",
        "id": 9,
        "cost": 45
    },
    {
        "name": "Khakra          ",
        "id": 10,
        "cost": 10
    },
]

final_list = []
count = input("How many items do you want to buy? ")
for i in range(int(count)):
    id = input(f"Enter the id of the item {i+1} you want to buy: ")
    
    for item in items_in_shop:
        if item["id"] == int(id):
            final_list.append(item)
            break
print("-------------------------")
print("      Reeve's Shop       ")
print("-------------------------")
total_cost = 0
for item in final_list:
    print(f"{item['name']}  |  ₹{item['cost']}")
    total_cost = total_cost + item["cost"]
sgst = (total_cost*2.5)/100
cgst = sgst
total_cost = total_cost + sgst + cgst*9
print("-------------------------")
print(f"SGST              |  ₹{sgst}")
print(f"CGST              |  ₹{cgst}")
print("-------------------------")
total_cost = total_cost/10
print(f"Total Cost: ₹{total_cost}")