t = int(input("Enter the Number of Buffets: "))
for _ in range(t):
    n = int(input("Enter the size of the Buffet: "))
    items = []
    for _ in range(n):
        value = input("Enter the Dish: ")
        items.append(value)
    dish_types = set(items)
    max_dishes = 0
    result = items[0]
    for dish in dish_types:
        count = 0
        i = 0
        while i < n:
            if items[i] == dish:
                count += 1
                i += 2  # Skip the next item
            else:
                i += 1
        if count > max_dishes or (count == max_dishes and dish < result):
            max_dishes = count
            result = dish
    print(result)

            
                         
      
            
                
        