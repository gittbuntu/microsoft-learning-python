guest_list = ["Noman","Bilal","Farhan"]

name = "Noman"
guest_list.remove(name)
guest_list.append("Ali")
print(guest_list)
print("we found a big table for dinner so we are inviting more guests")
guest_list.insert(0,"Warsi")
guest_list.insert(3,"Moazzam")
guest_list.append("Saad")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to dinner at my place.")

print(f"{name} is not available")

print(guest_list)
sorted_list = sorted(guest_list) #temporarily sorted list
print(sorted_list)
print(guest_list)
new_list = guest_list.sort() #permanently sorted list
print(new_list)