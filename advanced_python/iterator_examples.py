nums = [1, 2, 3]

it = iter(nums)

print(next(it))
print(next(it))

for x in it:
    print(x)

print(list(it))

text = "Hi"

it1 = iter(text)
it2 = iter(text)

print(next(it1))
print(next(it1))

print(next(it2))

print(next(it2))

nums = [100, 200]

it = iter(nums)

while True:
    try:
        value = next(it)
        print(value)
    except StopIteration:
        print("Finished!")
        break