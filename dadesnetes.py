file_path = '/home/jordina/Desktop/datathon/out.txt' 
codis_bcn = [8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009, 8010, 8011, 8012, 8013, 8014, 8015, 8016, 8017, 8018, 8019, 8020, 8021, 8022, 8023, 8024, 8025, 8026, 8027, 8028, 8029]

mitjadins = 0
mitjafora = 0

countdins = 0
countfora = 0

with open(file_path, 'r') as file:
    file_content = file.read()

    data = file_content.splitlines()
    i = 0
    for indx, line in enumerate(data, 0):
        if indx == 3*i+1:
            postal = int(line[-5:])
            if postal in codis_bcn:
                mitjadins += int(data[indx-1])
                countdins += 1
            else:
                mitjafora += int(data[indx-1])
                countfora += 1
            i += 1

# print(round(mitjadins/countdins, 3), round(mitjafora/countfora, 3))

minuts = []
with open(file_path, 'r') as file:
    file_content = file.read()

    data = file_content.splitlines()
    i = 0
    for indx, line in enumerate(data, 0):
        if indx == 3*i:
            x = int(line)
            postal = int(data[indx+1][-5:])
            if x > 0:
                minuts.append((x, postal))
            i += 1


def bubble_sort(data):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

m = bubble_sort(minuts)
minM = m[-45:-35]
print(minM)