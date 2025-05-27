import art
print(art.logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bid_dict = {}

re_run = True
while re_run:
    name = input("Please enter your name: ")
    bid_price = int(input("Please enter the amount you'd like to bid: $"))
    print("\n" * 20)

    bid_dict[name] = bid_price

    proceed = input("Are there more bidders to add? Type 'Y' for yes or 'N' for no.").lower()
    if proceed == 'n':
        print("Thanks for bidding!")
        re_run = False

highest_bid = 0
winners_name = ""

for bid in bid_dict:
    bid_price = bid_dict[bid]
    if bid_price > highest_bid:
        highest_bid = bid_price
        winners_name = bid
print(f"The winner is {winners_name} with a bid of ${highest_bid}!")

