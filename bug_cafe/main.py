DRINKS = [
    {"name": "コーヒー", "price": "300"},
    {"name": "カフェラテ", "price": "400"},
    {"name": "チャイ", "price": "460"},
    {"name": "エスプレッソ", "price": "340"},
    {"name": "緑茶", "price": "450"},
]

FOODS = [
    {"name": "チーズケーキ", "price": "470"},
    {"name": "アップルパイ", "price": "520"},
    {"name": "ホットサンド", "price": "410"},
]

def take_order(menus, order_number):
    for i, menu in enumerate(menus):
        print(f"({i + 1}) {menu['name']}: {menu['price']}円")
    print(f"> {order_number}")
    print(f"{menus[order_number]['name']}（{menus[order_number]['price']}円）ですね。")
    return order_number

print("ご注文を番号でどうぞ。")
order1 = take_order(DRINKS, 2)
print("フードメニューはいかがですか?")
order2 = take_order(FOODS, 1)

total = FOODS[order1]["price"] + DRINKS[order2]["price"]

print(f"お会計は{total}円になります。ありがとうございました！")
