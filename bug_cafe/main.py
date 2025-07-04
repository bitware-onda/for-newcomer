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
    print(f"{menus[order_number-1]['name']}（{menus[order_number-1]['price']}円）ですね。")
    return order_number-1

print("ご注文を番号でどうぞ。")
drink_order = take_order(DRINKS, 2)
print("フードメニューはいかがですか?")
food_order = take_order(FOODS, 1)

total = int(DRINKS[drink_order]["price"]) + int(FOODS[food_order]["price"])

print(f"お会計は{total}円になります。ありがとうございました！")
