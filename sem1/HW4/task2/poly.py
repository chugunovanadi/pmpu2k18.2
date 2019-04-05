from HW4.task2.poly_logic import read_poly, diff, poly2str

s = input("Введите полином")
polynom = read_poly(s)
print("Производная полинома:", poly2str(diff(polynom)))
