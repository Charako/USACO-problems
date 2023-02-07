"""
Each leader must have a list that includes all the cows of their breed, or the other breeds leader.

to find first instance use .find("G/H") and for the last instance  .rfind("G/H")

a general condition is that if the first instance of the cow does not have a list that includes up to the last instance,
then there is no leader of that breed as any cow after that cannot include the first instance. Do this for the other breed
and find the leader there.
"""
total = 0
N_input = int(input(""))
string_of_cows = input("")
cow_breeds = [x for x in string_of_cows]
cow_lists = list(map(int, input().split()))


sorted_cow_breeds = sorted(cow_breeds)

total_number_G = sorted_cow_breeds.index("H") - (sorted_cow_breeds.index("G") + 1) + 1
total_number_H = len(sorted_cow_breeds) - (sorted_cow_breeds.index("H") + 1) + 1

first_instance_G = string_of_cows.find("G")
first_instance_H = string_of_cows.find("H")

last_instance_G = string_of_cows.rindex("G") + 1
last_instance_H = string_of_cows.rindex("H") + 1

if cow_lists[first_instance_G] >= last_instance_G:
    for i in range(first_instance_G):
        if cow_breeds[i] == "H" and cow_lists[i] >= first_instance_G + 1:
            total +=1
if cow_lists[first_instance_H] >= last_instance_H:
    for i in range(first_instance_H):
        if cow_breeds[i] == "G" and cow_lists[i] >= first_instance_H + 1:
            total +=1

if cow_lists[first_instance_H] >= last_instance_H and cow_lists[first_instance_G] >= last_instance_G:
    total +=1

print(total)
