# app giai? phuong? trinh` bac. hai 
# viet' bang` python 

# ax^2 + bx + c
# ac = b1b2
# b1 + b2 = b

def giai():
	print("Ví dụ: x^2 + 5x + 6 ==> (x + 3)(x + 2)")
	print("")
	print("Note: Nhập xong 3 số a, b, c mà k có phương trình mới = phương trình vô nghiệm ! ")
	print("Phương trình có dạng: ax^2 + bx + c")
	a = int(input("Điền a = "))
	b = int(input("Điền b = "))
	c = int(input("Điền c = "))

	tich1 = a * c
	b1 = -100
	if a == 0 or b == 0:
		print("Phương Trình Vô Nghiệm ! ")
	else:
		
		if b > 0: 
			x = int(b/2)
		elif b <= 0:
			x = b / 2

		while b1 < x:
			b1 = b1 + 1 	
			b2 = b - b1
			if b1 * b2 == tich1:
				print("Phương Trình Mới:  (x + " + str(b1) + ")(x + " + str(b2) + ")")
				break

def ask():
	choice = input("Tiếp Tục? (Y/n): ")
	if choice == "Y" or choice == "y":
		print(".")
		print(".")
		giai()
	else:
		return 0
giai()
ask()