# # 클래스 정의(선언) :  붕어빵 틀

# class User:
#     def __init__ (self, name): # 생성자 : 클래스가 처음 생성될 떄 자동으로 호출
#         self.name = name # 변수를 초기화

#     def show(self): # 매서드(Method)
#         return f"회원 이름: {self.name}"

# # 인스턴스 생성: 붕어빵 만들기
# user_a = User("손흥민")
# user_b = User("이강인")

# # User 클래스로 생성한 인스턴스 (메모리에 생성)

# # 클래스의 인스턴스 변수
# print(user_a.name)
# print(user_b.name)

# print(user_a.show())
# print(user_b.show())

# print(type(user_a))
# print(user_a is user_b)
# print(id(user_a))
# print(id(user_b))

# # =======================================


# class Monitor:
#     def display_info(self):
#         # 인스턴스 변수
#         self.resolution = "1920x1080"
#         self.size = "27인치"
#         print(f"모니터 정보\n해상도: {self.resolution}\n크기: {self.size}\n객체 ID: {id(self)}")

# monitor = Monitor() # 인스턴스 생성 (모니터 객체 생성)
# print(id(monitor)) #모니터 인스턴스의 ID 출력

# monitor.display_info()


# # =======================================

# class SmartPhone:
#     def __init__(self, model):
#         self.battery = 50 # 속성 (aAttribute)
#         self.model = model # 속성 (aAttribute)

#     def charge(self, amount):
#         self.battery += amount
#         if self.battery > 100:
#             self.battery = 100
#             print(f"배터리 충전 완료 : {self.battery}%")
#         else:
#             print(f"배터리 충전 중 ... : {self.battery}%")

# phone_a = SmartPhone("아이폰")
# phone_b = SmartPhone("갤럭시")

# print(phone_a.model)
# print(phone_a.battery)
# phone_a.charge(30)
# phone_a.charge(30)

# 은행 계좌 클래스

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner # 계좌 소유주
        self.balance = balance # 계좌 잔액

    def __str__(self):
        return f"예금주 : {self.owner}, 잔액 : {self.balance:,}"

    def __repr__(self):
        return f"예금주 : {self.owner}, 잔액 : {self.balance:,}"


    # 입금 처리 매서드
    def deposit(self, amount):
        self.balance += amount # 입금처리
        print(f"{amount:,} 입금 완료 / 잔액 : {self.balance:,}원")

    # 출금 처리 매서드
    # 잔액 확인 => 잔액 부족시 경고 메시지 출력
    def withdrow(self, amount):
        if self.balance < amount:
            print("잔액이 부족합니다")
            return 0
        self.balance -= amount # 출금처리
        print(f"{amount:,} 출금 완료 / 잔액 : {self.balance}")

account_a = BankAccount("이수환", 100_000)
print(account_a)
account_a.deposit(500_000)
account_a.withdrow(1_000_000)
print(f"잔액 : {account_a.withdrow(200_000)}")
print(f"잔액 : {account_a.withdrow(400_000)}")

account_c = BankAccount("홍길동", 200_000)
print([account_a, account_c])
