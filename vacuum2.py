# تعریف ارایه دو بعدی
rooms = [[0, 0, 0, 1, 0],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1],
         [0, 0, 0, 0, 0]]

# پرسش از کاربر برای موقعیت جارو برقی
print("جارو برقی در کدام خانه از ارایه قرار دارد؟")
x = int(input("x: "))
y = int(input("y: "))

# متغیرهای مورد نیاز
num_rooms = 0
num_obstacles = 0
num_sweeps = 0

# حلقه های تو در تو برای پیمایش ارایه دو بعدی
for i in range(len(rooms)):
    for j in range(len(rooms[i])):
        if rooms[i][j] == 0:  # اتاق جدید
            num_rooms += 1
        elif rooms[i][j] == 1:  # موانع
            num_obstacles += 1
        elif i == x and j == y:  # جارو برقی
            num_sweeps += 1

            # عملیات مکش جارو برقی
            rooms[i][j] = 0

# چاپ نتیجه
print(f"تعداد اتاق ها: {num_rooms}")
print(f"تع
