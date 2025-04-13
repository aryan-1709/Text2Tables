from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')
    prompt=ChatPromptTemplate([
        ('system',prompt),
        ('human',question)
    ])
    parser = StrOutputParser()
    chain = prompt | model | parser
    response = chain.invoke({})
    return response
## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt = []

with open('database_info.txt') as f:
    prompt.extend(f.readlines())

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"Sales.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
