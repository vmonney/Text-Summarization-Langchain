"""Main app file for the Streamlit app."""

# Importing the dependencies
import os

import streamlit as st
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Setting the API key
os.environ["OPENAI_API_KEY"] = "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"

# Build up a chain
llm = OpenAI(temperature=0)

template = PromptTemplate(
    input_variables=["summary_block"],
    template="""Summarise the following block of text:
                          {summary_block}""",
)

chain = LLMChain(llm=llm, prompt=template)

# Writing Streamlit code
st.title("🤖 Summarization Streamlit App")

# Prompt bar
prompt = st.chat_input("Enter the text you want to summarize")

# Trigger if user presses enter
if prompt:
    # Display the prompt back to the screen
    st.chat_message("human", avatar="🎅").markdown(prompt)

    # Get the response from the LLM
    response = chain.run(prompt)

    # Display LLM output back to the screen
    st.chat_message("bot", avatar="🤖").markdown(response)
