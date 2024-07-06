import csv
import pandas as pd
from pandas import *
import get_all as gg

# results = pd.read_csv("user_database.csv")
# filename = "user_database.csv"
# uname=input("usern")
# password=input("pass")
# name=input('name')
# id=len(results)+1
# email=input('email')
# phone=input('phone')
# row=[id,name,uname,password,phone]
# with open(filename, 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow(row)
#

# def get_existing_users():
#     # filename = 'user_database.csv'
#     # with open(filename, 'r') as f:
#     #     uname_data = [(line['email']) for line in csv.DictReader(f)]
#     #     password_data=[(line['Username']) for line in csv.DictReader(f)]
#     #     return uname_data,password_data
#     data = read_csv("user_database.csv")
#     uname = data['email'].tolist()
#     up = data['Username'].tolist()
#     return (uname,up)
#
#
# lis= get_existing_users()
# uname='abd77044'
# password='77044'
#
# print(lis)
# # print(up)

#
# def func():
#     statement=int(input("please enter the numnber\n 1.get latest stocks\n2.get most active stocks\n3.get top stock "
#                         "gainers\n4.get top stock losers\n5.get stock data"))
#     match statement:
#         case 1:
#             gg.get_trending_stocks()
#         case 2:
#             gg.get_most_active_stocks()
#         case 3:
#             gg.get_top_stock_gainers()
#         case 4:
#             gg.get_top_stock_losers()
#         case 5:
#             url = input("give url")
#             gg.get_stock_data(url)
#         case unknown_input:
#             print(f"invalid input:{unknown_input}")
#
# func()
# import user as u

# def user_side_start():
#     while True:
#         print("Welcome page")
#         username = input("username?")
#         un_data, up_data = u.get_existing_users()
#         if username not in un_data:
#             print('not found')
#             # obj.create_new_user()
#         else:
#             password = input("password?")
#             if u.check_validity(username, password):
#                 # obj.user_menu()
#                 print('yes')
#                 break
#             else:
#                 pass
#
# print(u.get_existing_users())

#
# from datetime import date
#
# today = date.today()
# print("Today's date:", today)

x=1
y=5

x+= ++x + y-- * x++ + y++