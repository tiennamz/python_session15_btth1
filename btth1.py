inventory_stock = 100 
total_revenue = 0.0
discount = 0.1
'''
Chức năng 1: Nhập thêm hàng vào kho 

Yêu cầu người dùng nhập số lượng hàng muốn thêm. 

Gọi hàm add_stock(amount) để cộng thêm số lượng này vào biến toàn cục inventory_stock.

Cần sử dụng từ khóa global bên trong hàm.

Trường hợp nhập hàng hợp lệ:

Chọn chức năng (1-4): 1
--- NHẬP HÀNG ---
Nhập số lượng sản phẩm muốn thêm: 50
Đã nhập thành công 50 sản phẩm.
Tồn kho hiện tại: 150

'''
def standardization_number(number):
    """Hàm giúp chuẩn hóa str thành int nếu hợp lệ

    Args:
        number (str): số trc khi đc ép kiểu

    Returns:
        int: số sau khi đc ép kiểu
    """
    try:
        number = int(number)
        return number
    except:
        print("Lỗi nhập số")
        return False
        
    
def add_stock(amount):
    if standardization_number(amount) == False:
        return False
        
    if amount <= 0:
        print("Số lượng nhập vào phải là số nguyên dương")
        return False
    else:
        return amount

'''
Chức năng 2: Bán hàng

Yêu cầu người dùng nhập số lượng sản phẩm muốn mua và đơn giá của một sản phẩm.
'''
def calculate_final_price(quantity, price):

    total_money = quantity * price
        
    return total_money

'''
Chức năng 3: Xem báo cáo tổng quan

Gọi hàm print_report(). Hàm này phải chứa Docstring mô tả chi tiết chức năng của nó.

Hàm in ra trạng thái của 2 biến toàn cục.

Chọn chức năng (1-4): 3
--- BÁO CÁO KINH DOANH ---
Tồn kho hiện tại: 140 sản phẩm
Tổng doanh thu: $1458.0
'''
def print_report(quantity, price):
    """Hàm dùng để in ra báo cáco số lượng hàng hiện tại và số tiền bán đc

    Args:
        quantity (int): số lượng hiện tại
        price (int): số tiên kiếm được
    """
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {quantity} sản phẩm")
    print(f"Tổng doanh thu: ${price}")

while True:
    choice = input('''
========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
Chọn chức năng (1-4): ''')
    
    match choice:
        case '1':
            amount_inp = input("Nhập số lượng sản phẩm muốn thêm: ")
            if standardization_number(amount_inp) == False:
                continue
            amount_inp = int(amount_inp)
            if add_stock(amount_inp) != False:
                inventory_stock += amount_inp
            else:
                continue
            print(f"Đã nhập thành công {amount_inp} sản phẩm.")
            print(f"Tồn kho hiện tại: {inventory_stock}")
            
        case '2':
            print("--- BÁN HÀNG ---")
            quantity_inp = input("Nhập số lượng mua: ")
            if standardization_number(quantity_inp) == False:
                continue
            elif  int(quantity_inp) > inventory_stock:
                print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
                continue
            inventory_stock -= int(quantity_inp)
            price_inp = input("Nhập đơn giá ($): ")
            if standardization_number(price_inp) == False:
                continue
            print("-> Hóa đơn chi tiết:")
            print(f"Số lượng: {quantity_inp} | Đơn giá: ${price_inp}")
            total_revenue = calculate_final_price(int(quantity_inp), int(price_inp))
            print(f"Tạm tính: ${total_revenue}")
            print(f"Giảm giá (10%): ${total_revenue * discount}")
            vat = (total_revenue - total_revenue * discount) * 0.08
            print(f"Thuế VAT (8%): ${vat}")
            total_revenue = total_revenue - total_revenue * discount + vat
            print(f"Tổng thanh toán: ${total_revenue}")
            print("Đã bán thành công!")
        
        
        case '3':
            print_report(inventory_stock, total_revenue)
            
        case '4':
            print("Thoát chương trình")
            break
        case _:
            print("Lỗi cú pháp")