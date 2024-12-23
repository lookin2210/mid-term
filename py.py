width = float(input())
length = float(input())
depth = float(input())
volume = width * length * depth
time_in_minutes = (volume * 15) / 60
print(f"ต้องใช้เวลาในการเติมน้ำ {time_in_minutes:.2f} นาที")
