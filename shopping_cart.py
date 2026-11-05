


# shopping cart 클래스 생성

class ShoppingCart:
    # def __init__(self, items, price):
    #     self.items = items
    #     self.price = price

# 상품 목록 저장 기능
# 매서드
# - 장바구니 담기
# - 장바구니 빼기
# - 상품 목록 조회

    def __init__(self):
        self.items = []
        self.price = 0

    def __str__(self):
        result =  "현재 장바구니에 들어있는 상품\n"
        for item in self.items:
            result += f"{item.name}: {item.price}원\n"
        result += f"총 가격: {self.price}"
        return result 

    def show_items(self):
        return self.items

    def add_item(self, items):
        self.items.append(items)
        self.price += items.price

    def remove_item(self, items):
        self.items.remove(items)
        self.price -= items.price

# 상품 클래스
# 속성
# - 제품명
# - 가격
class item:
    def __init__(self, name, price):

        self.name = name
        self.price = price

# 상품 3개 생성
item_apple = item("사과", 3_000)
item_banana = item("바나나", 2_000)
item_beer = item("맥주", 4_000)

# shopping cart 생성
cart_a = ShoppingCart() 

# 상품 1개 장바구니 담기
cart_a.add_item(item_apple)

# 상품 1개 장바구니 담기
cart_a.add_item(item_banana)

# 상품 1개 장바구니에서 빼기
cart_a.remove_item(item_banana)

cart_a.add_item(item_beer)
# 장바구니에 담긴 상품 목록 조회
for item in cart_a.show_items():
    print(item.name, item.price)

print(cart_a)
print(cart_a.show_items)