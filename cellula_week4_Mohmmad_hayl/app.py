import streamlit as st
from llm.llm_engine import LLMEngine
from llm.router import Router

st.title("LLM Engine Assistant")

@st.cache_resource
def load_router():
    engine = LLMEngine()
    return Router(engine)

router = load_router()

if "pending_query" not in st.session_state:
    st.session_state.pending_query = None

user_input = st.text_area("Enter your request:")

if st.button("Submit"):
    if user_input.strip():
        with st.spinner("Processing..."):
            response = router.classify(user_input)

        if response["task"] == "generate" and response["result"]["status"] == "needs_input":
            st.session_state.pending_query = response["result"]["query"]
            st.warning("No suitable answer found in the database.")
        else:
            st.session_state.pending_query = None
            if response["task"] == "generate":
                st.code(response["result"]["code"], language="python")
                st.text("Output:")
                st.text(response["result"]["output"])
            else:
                st.write(response["result"])
    else:
        st.warning("Please enter a request.")

if st.session_state.pending_query:
    st.write(f"Question: {st.session_state.pending_query}")
    user_code = st.text_area("Enter the correct Python code:", key="user_code_input")

    if st.button("Save and Run"):
        result = router.generator.save_and_run(
            st.session_state.pending_query, user_code
        )
        st.session_state.pending_query = None
        st.code(result["code"], language="python")
        st.text("Output:")
        st.text(result["output"])