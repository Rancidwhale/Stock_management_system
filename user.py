import csv
import sys
import samp1
import tkinter as tk
import tkinter.messagebox
import pandas as pd
import mysql.connector as cc
import get_all as gg
from pandas import *
from datetime import date



def get_existing_users():
    # filename = 'user_database.csv'
    # with open(filename, 'r') as f:
    #     uname_data = [(line['email']) for line in csv.DictReader(f)]
    #     password_data = [(line2['Username']) for line2 in csv.DictReader(f)]
    #     print(uname_data)
    #     print(password_data)
    #     return uname_data, password_data
    data = read_csv("user_database.csv")
    uname = data['Username'].tolist()
    up = data['Password'].tolist()
    return uname, up


def check_validity(un, up):
    l1, l2 = get_existing_users()
    r = l1.index(un)
    if str(l2[r]) == str(up):
        return True
    else:
        return False
    # list1, list2 = get_existing_users()
    # merged_list = tuple(zip(list1, list2))
    # print(str(merged_list))
    # if (un, up) in merged_list:
    #     print('correct')
    #     return True
    # else:
    #     return False


def display_csv(name):

    if name in ['trending_stock_info.csv', 'most_active_stock_info.csv', 'top_stock_gainers_info.csv', 'top_stock_losers_info.csv']:
        samp1.displayss(name)
    else:
        df = pd.read_csv(name)
        print(df)



def getcomp():
    try:
        data = read_csv("company.csv")
    except pd.io.common.EmptyDataError:
        return []

    cname = data['company_name'].tolist()
    return cname


class DBMS:
    def __init__(self):
        self.con = cc.connect(host='localhost',
                              port='3306',
                              user='root',
                              password='ABD@root77',
                              database='project')
        query = 'create table if not exists user_list (id int primary key,name varchar(20),email varchar(50),' \
                'username varchar(35),password varchar(30),phone varchar(10))'
        query2 = 'create table if not exists company (company_name varchar(30)primary key,Count varchar(2))'
        query3 = 'create table if not exists analyst_suggestion (company_name varchar(30) primary key,BuySell varchar(10))'

        query4 = 'create table if not exists purchase (username varchar(30),company varchar(30),date date);'
        cur = self.con.cursor()
        cur.execute(query2)
        cur.execute(query)
        cur.execute(query3)
        cur.execute(query4)
        row=['company_name']
        with open('company.csv', 'a') as f:
            pass
        f.close()


    def create_new_user(self):
        self.con = cc.connect(host='localhost',
                              port='3306',
                              user='root',
                              password='ABD@root77',
                              database='project')
        results = pd.read_csv("user_database.csv")
        filename = "user_database.csv"
        name = input('Name')
        uname = input("Username")
        password = input("password?")
        email = input('email')
        phone = input('phone')
        id = len(results) + 1
        row = [id, name, email, uname, password, phone]
        with open(filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(row)

        query = "INSERT INTO user_list VALUES "+str(tuple(row))+";"
        cur = self.con.cursor()
        cur.execute(query)

        filename_forcsv = uname+'.csv'
        user_stock_header = ['Company_name', 'Price', 'Change']
        # user_stock_header.to_csv(filename_forcsv, index=False)
        with open(filename_forcsv,'a') as f:
            writer = csv.writer(f)
            writer.writerow(user_stock_header)

        query2 = "CREATE TABLE IF NOT EXISTS "+uname+" (Company_name varchar(50) primary key,price varchar(10),price_change varchar(10));"
        cur.execute(query2)


    def user_menu(self,uname):
        self.con = cc.connect(host='localhost',
                              port='3306',
                              user='root',
                              password='ABD@root77',
                              database='project')
        statement = int(
            input("Please enter the Choice\n 1.Trending stocks\n2.Most Active stocks\n3.Top "
                  "Gainers\n4.top Losers\n5.Your stocks\n6.Analyst suggestion\n7.exit\n8.login"))
        match statement:
            case 1:
                gg.get_trending_stocks()
                display_csv('trending_stock_info.csv')
                self.user_menu(uname)
            case 2:
                gg.get_most_active_stocks()
                display_csv('most_active_stock_info.csv')
                self.user_menu(uname)
            case 3:
                gg.get_top_stock_gainers()
                display_csv('top_stock_gainers_info.csv')
                self.user_menu(uname)
            case 4:
                gg.get_top_stock_losers()
                display_csv('top_stock_losers_info.csv')
                self.user_menu(uname)
            case 5:
                self.user_stocks(uname)

            case 6:
                display_csv('analyst.csv')
                self.user_menu(uname)
            case 7:
                sys.exit()
            case 8:
                user_side_start()
            case unknown_input:
                print(f"invalid input:{unknown_input}")

    def user_stocks(self,
                    uname):
        self.con = cc.connect(host='localhost',
                              port='3306',
                              user='root',
                              password='ABD@root77',
                              database='project')
        name = uname + '.csv'
        display_csv(name)
        ch = int(input("Enter choice\n\n1.Add more \n2.delete\n3.go back to menu "))
        match ch:
            case 1:
                url = input('Url of stock to add')
                info = gg.get_stock_data(url)
                info[0]=str(info[0])
                info[1]=str(info[1])
                info[2]=str(info[2])
                print(len(info))
                print(info)
                with open(name, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(info)
            #             also add query to add into database
                query_insert = "INSERT INTO " + uname + " VALUES "+str(tuple(info))+";"
                # print("added into csv")
                # print(query_insert)
                cur2 = self.con.cursor()
                cur2.execute(query_insert)
                self.con.commit()
                # print("added into database")
                today =str(date.today())
                a = (uname, info[0], today)
                qq="INSERT INTO PURCHASE VALUES "+str(tuple(a))
                cur3 = self.con.cursor()
                cur3.execute(qq)
                self.con.commit()
                comp = getcomp()
                cname = info[0]
                if info[0] not in comp:
                    with open('company.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([info[0], '1'])

                    query2 = 'INSERT INTO company VALUES'+str(tuple([info[0], '1']))+';'
                    cur2.execute(query2)
                    self.con.commit()
                else:
                    query2 = "UPDATE company SET Count = Count + 1 WHERE company_name=\""+info[0]+"\";"
                    cur2.execute(query2)
                    self.con.commit()
                    cur3 = self.con.cursor()
                    cur3.execute("SELECT COUNT FROM company where company_name=\""+info[0]+"\";")

                    c = cur3.fetchall()
                    df = pd.read_csv('company.csv')
                    df = df[df.company_name != cname]

                    df.to_csv('company.csv', index=False)
                    row = [cname,c[0][0]]
                    with open('company.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow(row)

                self.user_menu(uname)

            case 2:
                cname = input("Company name to delete")
                df = pd.read_csv(name)
                df = df[df.Company_name != cname]

                df.to_csv(name, index=False)
                query = "DELETE FROM "+uname+" WHERE Company_name =\""+cname+"\";"
                cur = self.con.cursor()
                cur.execute(query)
                self.con.commit()

                cur3 = self.con.cursor()
                cur3.execute("SELECT COUNT FROM company where company_name=\"" + cname + "\";")
                c = cur3.fetchall()
                c1=int(c[0][0])
                if c1 > 1:
                    cur2 = self.con.cursor()
                    query2 = "UPDATE company SET Count = Count - 1 WHERE company_name=\"" + cname + "\";"
                    cur2.execute(query2)
                    self.con.commit()

                    df = pd.read_csv('company.csv')
                    df = df[df.company_name != cname]

                    df.to_csv('company.csv', index=False)
                    with open('company.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([cname, c1-1])
                else:
                    query5 = "DELETE FROM company WHERE company_name =\"" + cname + "\";"
                    cur3.execute(query5)
                    self.con.commit()
                    df = pd.read_csv('company.csv')
                    df = df[df.company_name != cname]

                    df.to_csv('company.csv', index=False)


                self.user_menu(uname)



            case 3:
                self.user_menu(uname)

            case unknown_input:
                print(f"invalid input:{unknown_input}")
                self.user_menu(uname)


obj = DBMS()
username = ''
password = ''


def analystfunc():
    con = cc.connect(host='localhost',
                              port='3306',
                              user='root',
                              password='ABD@root77',
                              database='project')

    # pass1 = input('password?')
    # if pass1 != '2002':
    #     print('invalid')
    #     user_side_start()
    display_csv('analyst.csv')
    ch = int(input("1.Add Stock\n2.Delete Stock\n3.Delete all\n4.exit\n5.back to login"))
    match ch:
        case 1:
            st = input("Enter stock name to add")
            dec = input("buy/sell")
            # with open('analyst.csv', "r") as f:
            #     reader = csv.reader(f, delimiter=",")
            #     data = list(reader)
            #     row_count = len(data)
            # row = [row_count, st, dec]
            row = [st, dec]
            with open('analyst.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(row)

            query = 'INSERT INTO analyst_suggestion VALUES'+str(tuple(row))+';'
            cur = con.cursor()
            cur.execute(query)
            con.commit()

            analystfunc()

        case 2:
            cname = input("Company name to delete")
            df = pd.read_csv('analyst.csv')
            df = df[df.Company_name != cname]

            df.to_csv('analyst.csv', index=False)

            query = 'DELETE FROM analyst_suggestion WHERE company_name=\"'+cname+'\";'
            cur = con.cursor()
            cur.execute(query)
            con.commit()
            analystfunc()

        case 3:
            query = 'TRUNCATE TABLE analyst_suggestion;'
            cur = con.cursor()
            cur.execute(query)
            con.commit()

            f = open("analyst.csv", "w")
            f.truncate()
            f.close()
            row =['Company_name','Buy/Sell']
            with open('analyst.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(row)
            analystfunc()

        case 4:
            sys.exit()

        case 5:
            user_side_start()


def user_side_start():
    while True:
        print("Welcome page")
        username = input("username?")
        if(username == 'akash2002'):
            pass1 = input("password?")
            if pass1 == '2002':
                analystfunc()
            break
        un_data, up_data = get_existing_users()
        if username not in un_data:

            obj.create_new_user()
        else:
            password = input("password?")
            if check_validity(username, password):
                obj.user_menu(username)
                break
            else:
                pass






