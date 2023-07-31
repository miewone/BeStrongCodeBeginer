record = int(input())
record_list = list(map(int, input().split()))
max_record = max(record_list)

new_list =[ ]
for score in record_list :
    new_list.append(score/max_record * 100)
record_avg = sum(new_list)/record
print(record_avg)
