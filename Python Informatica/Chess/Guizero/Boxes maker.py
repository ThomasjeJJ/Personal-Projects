boxes = []

for i in range(0,8):
    for q in range (0,8):
        boxes.append(f"box{i}_{q} = Box(app. layout='grid'. grid=[{i}.{q}]. border=1)")

print(boxes)

