import streamlit as st
try:
    st.title("BASIC CALCULATOR APP")

    user_option = st.multiselect("Choose an operand", ["ADDITION", "SUBTRACTION", "MULTIPLICATION", "DIVISION","MODULUS"])


    def addition():
        a = st.number_input("Enter Your value: ", key="<one>")
        b = st.number_input("Enter Your value: ", key="<two>")
        answer = a + b
        if a + b:
            st.write(f"{a} + {b} = {answer:.1f}")


    def subtraction():
        a = st.number_input("Enter Your value: ", key="<three>")
        b = st.number_input("Enter Your value: ", key="<four>")
        answer = a - b
        if a - b:
            st.write(f"{a} - {b} = {answer:.1f}")


    def multiplication():
        a = st.number_input("Enter Your value: ", key="<five>")
        b = st.number_input("Enter Your value: ", key="<six>")
        answer = a * b
        if a * b:
            st.write(f"{a} * {b} = {answer:.1f}")


    def division():
        a = st.number_input("Enter Your value: ", key="<seven>")
        b = st.number_input("Enter Your value: ", key="<eight>")
        answer = a / b
        if a / b:
            st.write(f"{a} / {b} = {answer:.1f}")


    def modulus():
        a = st.number_input("Enter Your value: ", key="<nine>")
        b = st.number_input("Enter Your value: ", key="<ten>")
        answer = a % b
        if a % b:
            st.write(f"{a} % {b} = {answer:.1f}")


    if "ADDITION" in user_option:
        st.info("You selected ADDITION")
        addition()
    elif "SUBTRACTION" in user_option:
        st.info("You selected SUBTRACTION")
        subtraction()
    elif "MULTIPLICATION" in user_option:
        st.info("You selected MULTIPLICATION")
        multiplication()
    elif "DIVISION" in user_option:
        st.info("You selected DIVISION")
        division()
    elif "MODULUS" in user_option:
        st.info("You selected MODULUS")
        modulus()

except ZeroDivisionError:
    st.info("Enter Your Figures")
