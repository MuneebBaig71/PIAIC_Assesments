def triple(input_l,data):
    for i in range(3):
        input_l.append(data)

    return input_l
empty = []
data = "Hello"

print(triple(empty,data))
