import streamlit as st

# set the app title
st.title("This is a title")

#this is how you "write"
st.write("This is a text")

#adding a button
st.button("Reset", type="primary")
if st.button("Say Hello"):
    st.write("Why hello there!")
    st.balloons()
    st.image('https://handletheheat.com/wp-content/uploads/2015/03/Best-Birthday-Cake-with-milk-chocolate-buttercream-SQUARE.jpg')
    st.image('cat.png')
else:
    st.write("Goodbye!")