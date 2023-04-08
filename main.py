import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.set_page_config(page_title="Library Management System",page_icon="https://www.pngitem.com/pimgs/m/32-327951_events-learning-circle-icon-library-management-system-icon.png")
st.title(":blue[LIBRARY MANAGEMENT SYSTEM]")
st.sidebar.image("https://www.skoolbeep.com/blog/wp-content/uploads/2020/12/HOW-DO-YOU-DESIGN-A-LIBRARY-MANAGEMENT-SYSTEM-min.png")
choice=st.sidebar.selectbox("MY MENU",("HOME","STUDENT LOGIN","LIBRARIAN LOGIN"))
if(choice=="HOME"):
    st.markdown("<center><img src='https://www.clipartmax.com/png/full/142-1429304_library-management-library-management-system-png.png'></center>",unsafe_allow_html=True)
    st.markdown("<center><h1>WELCOME</h1></center>",unsafe_allow_html=True)
    st.write("1.It is a Web Application which manages the data of Books, Issue Books,Student, Librarian so that the features such as Viewing Books,Issue the Books, Add the Books, Login ,etc can be performed.It uses Database Management System (DBMS) such as MySQL , Oracle Database, Microsoft SQL Server .This Application can be accessed over a LAN (Local Area Network).")
    st.write("2.This Application is developed by Bhavana as a part of Training Project")
elif(choice=="STUDENT LOGIN"):
    st.markdown("<center><h1>HELLO STUDENT</h1></center>",unsafe_allow_html=True)
    if 'login' not in st.session_state:
        st.session_state['login']=False 
    sid=st.text_input("Enter Student ID")
    pwd=st.text_input("Enter Student Password")
    btn=st.button("LOGIN")
    btn2=st.button("LOGOUT")
    if btn2:
        st.session_state['login']=False
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="Mahadev",database="lms")
        c=mydb.cursor()
        c.execute("select * from students")
        for row in c:
            if(row[0]==sid and row[2]==pwd):
                st.session_state['login']=True
                break
        if(st.session_state['login']==False):
            st.error("Incorrect ID or Password")
    if st.session_state['login']:
        st.success("Login Successful")
        if st.session_state['login']==btn:
            st.balloons()
        choice2=st.selectbox("Features",("None","View All Books","Issue Books","New requirement"))
        if choice2=="View All Books":
            mydb=mysql.connector.connect(host="localhost",user="root",password="Mahadev",database="lms")
            c=mydb.cursor()
            c.execute("select * from books")
            l=[]
            for row in c:
                l.append(row)
            df=pd.DataFrame(data=l,columns=['Book ID','Book Name','Author Name'])
            st.dataframe(df)
        elif choice2=="Issue Books":
            bid=st.text_input("Enter Book ID")
            stid=st.text_input("Enter Your Student ID")
            btn3=st.button("Issue Book")
            if btn3:
                doi=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost",user="root",password="Mahadev",database="lms")
                c=mydb.cursor()
                c.execute("insert into issue values(%s,%s,%s)",(doi,bid,stid))
                mydb.commit()
                st.success("Book Issued Successfully")
        elif choice2=="New requirement":
            req=st.text_input("Enter the Book")
            auth=st.text_input("author name")
            btn4=st.button("Enter")
            if btn4:
                mydb=mysql.connector.connect(host="localhost",user="root",password="Mahadev",database="lms")
                c=mydb.cursor()
                c.execute("insert into newreq values(%s,%s)",(req,auth))
                mydb.commit()
                st.success("input taken")
 
elif(choice=="LIBRARIAN LOGIN"):
    st.markdown("<center><h1>HELLO LIBRARIAN</h1></center>",unsafe_allow_html=True)
    if 'llogin' not in st.session_state:
        st.session_state['llogin']=False
    if st.session_state['llogin']==False:
        sid=st.text_input("Enter Librarian ID")
        pwd=st.text_input("Enter Librarian Password")
        btn=st.button("LOGIN")
        btn2=st.button("LOGOUT")
        if btn2:
            st.session_state['llogin']=False
        if btn:
            mydb=mysql.connector.connect(host="localhost",user="root",password="Mahadev",database="lms")
            c=mydb.cursor()
            c.execute("select * from librarian")
            for row in c:
                if(row[0]==sid and row[1]==pwd):
                    st.session_state['llogin']=True
                    break
            if(st.session_state['llogin']==False):
                st.header("Incorrect ID or Password")
    if st.session_state['llogin']:
        st.header("Login Successful")
        choice2=st.selectbox("Features",("None","View Issue Books","Add new Books"))
        if choice2=="View Issue Books":
            mydb=mysql.connector.connect(host="localhost",user="root",password="Mahadev",database="lms")
            c=mydb.cursor()
            c.execute("select * from issue")
            l=[]
            for row in c:
                l.append(row)
            df=pd.DataFrame(data=l,columns=['Date of Issue','Book ID','Student ID'])
            st.dataframe(df)
        elif choice2=="Add new Books":
            bid=st.text_input("Enter Book ID")
            bname=st.text_input("Enter Book Name")
            aname=st.text_input("Enter Author Name")
            btn3=st.button("Add new Book")
            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="Mahadev",database="lms")
                c=mydb.cursor()
                c.execute("insert into books values(%s,%s,%s)",(bid,bname,aname))
                mydb.commit()
                st.header("Book Added Successfully")
