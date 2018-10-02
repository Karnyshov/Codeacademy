"""Define a function compute_bill that takes one argument food as input.
In the function, create a variable total with an initial value of zero.
For each item in the food list, add the price of that item to total.
Finally, return the total.
Ignore whether or not the item you're billing for is in stock.Note that your function should work for any food list."""

# Write your code below!
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total = 0
    for x in prices:
        if food[x] == "banana" or food[x] == "orange":
            total += prices[x]
        elif x == "apple":
            total += prices[x]
    print(total)
    return total  # Returns 7.5 instead of 2 ???
