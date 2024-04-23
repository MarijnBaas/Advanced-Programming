source = '3 2 1 4 8 7 6 5 9'
target = '1 2 3 4 5 6 7 8 9'

source_list = source.split()
for i in range(len(source_list)):
    source_list[i] = int(source_list[i])

target_list = target.split()
for i in range(len(target_list)):
    target_list[i] = int(target_list[i])

mutation = []
for i in range(len(source_list)):
    if source_list[i] != target_list[i]:
        mutation.append(source_list[i])

print(mutation)
