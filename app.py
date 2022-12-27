import streamlit as st
import math
import webbrowser

st.title("KITSW Internal Marks Calculator")

MSE1 = st.number_input("Enter MSE1 Marks:",max_value=30,min_value=0)
MSE2 = st.number_input("Enter MSE2 Marks:",max_value=30,min_value=0)
A1 = st.number_input("Enter A1 Marks:",max_value=10,min_value=0)
A2 = st.number_input("Enter A2 Marks:",max_value=10,min_value=0)
CP1 = st.number_input("Enter CP1 Marks:",max_value=10,min_value=0)
CRP1 = st.number_input("Enter CRP1 Marks:",max_value=10,min_value=0)
Minor1 = st.number_input("Enter Minor1 Marks:",max_value=10,min_value=0)
Minor2 = st.number_input("Enter Minor2 Marks:",max_value=10,min_value=0)

MSE = math.ceil((max(MSE1,MSE2)*0.7)+(min(MSE1,MSE2)*0.3))
TA = math.ceil((A1+A2+CP1+CRP1+Minor1+Minor2)/6)
Total = MSE+TA

if st.button("Calculate"):
    st.write("MSE:", MSE, "of 30 Marks")
    st.write("TA:", TA, "of 10 Marks")
    st.write("Total:", Total,"of 40 Marks")
    if Total >= 35:
        st.snow()
        st.success("Congratulations! You Scored Best Marks.")
    elif Total >= 30:
        st.success("Congratulations! You Scored Good Marks.")
        st.snow()
    elif Total >= 25:
        st.success("Congratulations! You Scored Average Marks.")
        st.snow()
    else:
        st.error("Oops! You Scored Poor Marks.")
        st.balloons()

st.sidebar.title("Support the Developer")
st.sidebar.markdown("If you find this app useful, you can buy me a coffee to show your appreciation.")
if (st.sidebar.button("Buy me a coffee")):
    st.sidebar.success("Thank you for your support!")
    url = 'https://svgshare.com/getbyhash/sha1-rdYGMpFqiLA6sONyyCQ+wyOLj2Y='
    webbrowser.open_new_tab(url)