from art import logo
from replit import clear
import getpass

print(logo)
auctioneers = []

while True:
    auctioneer = {}
    auctioneer["name"] = input("What is your name?: ")
    auctioneer["bid"] = float(getpass.getpass(prompt="What's your bid?: $"))
    check = input("Do you want to check the entered data? Type 'yes' or no. ").lower()
    if check == "yes" or check == "y":
        print("Please check that nobody is around to see.")
        print(f"Your name is {auctioneer['name'].title()} and your bid is ${auctioneer['bid']:.2f}")
    confirmation = input("Do you confirm the entered data? Type 'yes' or 'no'. ").lower()
    if confirmation == "yes" or check == "y":
        auctioneers.append(auctioneer)
    else:
        continue
    more_entries = input("\nAre there any other bidders? Type 'yes' or 'no'. ").lower()
    if more_entries == "yes" or more_entries == 'y':
        clear()
        continue
    else:
        break

biggest_bidder = {
        'name': "",
        'bid': 0
        }
for bidder in auctioneers:
    if bidder['bid'] > biggest_bidder['bid']:
        biggest_bidder = bidder

print(f"The winner is {biggest_bidder['name'].title()} with a bid of ${biggest_bidder['bid']}.")
