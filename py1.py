midterm = float(input())
final = float(input())
if 0 <= midterm <= 60 and 0 <= final <= 60:
    total = midterm + final
    average = total / 2
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
else:
    print("คะแนนที่ป้อนต้องอยู่ในช่วง 0.0 ถึง 60.0 เท่านั้น")
