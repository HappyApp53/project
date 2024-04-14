# The following program transfers NFT ownership.
from datetime import datetime
from update_accounts import *
from Tokens import *

timestamp = datetime.now().strftime("%B %d, %Y %H:%M:%S")


def transferOwnership(seller_money, buyer_money, new_owner):
    asset_info = []
    file = open("Ethereum-NFT.txt", "r")

    for i in file:
        info = i.replace("\n", "")
        asset_info.append(info)

    price = int(asset_info[4])

    if buyer_money >= price:
        updateUser2(buyer_money - price)
        updateUser1(seller_money + price)

        with open('Piskel-NFT.txt', 'w') as file:
            file.write(new_owner + "\n")
            file.write(asset_info[1] + "\n")
            file.write(asset_info[2] + "\n")
            file.write(asset_info[3] + "\n")
            file.write(nft_token())

        print("\n" + "------------------------------------")
        print("NFT Transferred!" + "\n" + timestamp)
        print("------------------------------------")
    else:
        print("Insufficient Funds!")
# 's Account Update

# The following program creates an account to store user2's crypto wallet.
from user_1 import *
from Transfer_funds import *
from nft_ownership import *

# Store Information
print("----------------------------------------------")
print("User Login")
print("----------------------------------------------")

user2_file = open("user2.txt", "r")
user2_info = []
for i in user2_file:
    data = i.replace("\n", "")
    user2_info.append(data)

user2_public_key = int(user2_info[3])
user2_private_key = int(user2_info[4])
user2_money = int(user2_info[5])

# User Login
user2_name = input("Name: ")
user2_username = input("Username: ")
user2_password = input("Password: ")

if user2_name == user2_info[0] and user2_username == user2_info[1] and user2_password == user2_info[2]:
    print("\n" + "--------------")
    print(user2_name + "'s Account")
    print("--------------")
    print("Account Balance: " + str(user2_money) + " coins")
    print("Public Key: " + str(user2_public_key))

    print("\n" + "What would you like to do?")
    print("a - Transfer Funds")
    print("b - Buy an NFT")

    to_do = input("Pick an option: ")

    if to_do == "a":
        transfer(user1_name, user1_money, user2_name, user2_money, user2_private_key, user2_public_key, 50)
    elif to_do == "b":
        transferOwnership(user1_money, user2_money, user2_name)
    else:
        print("No transactions in progress!")

else:
    print("\n" + "Invalid Username/Password, try again!")
    quit()