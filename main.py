import streamlit as st
from chain import run_chain
from schema import AboutProduct

st.title("Product Info Chatbot 💬")

user_input = st.text_input("Ask about a product:", "")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        try:
            result: AboutProduct = run_chain(user_input)
            st.subheader("Product Info (JSON)")
            # st.json(result.dict())
            st.json(result)
        except Exception as e:
            st.error(f"Error: {e}")
