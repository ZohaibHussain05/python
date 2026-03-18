bicycle = ['trek', 'redline', 'canonable', 'specialized']
print(bicycle[-1])

message = f"my first bicycle was {bicycle[0].title()}."
print(message)

names = ["ali", "butt", "shera"]
names.append("annus")
names.insert(0,"suleman")
names.insert(1,"fawad")
# del names[1]
# for name in names:
#     print(f"Hello {name}")

# last_friend = names.pop()
# print(f"My last friend name was {last_friend}")

# first_friend = names.pop(0)
# print(f"My first friend name waas {first_friend}")

# names.remove('ali') # remove only first instance with that value
# print(f"remaining freinds in list {names}")


names.sort()
print(names)

names.sort(reverse=True)
print(names)

print(len(names))