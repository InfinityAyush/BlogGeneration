import streamlit as st
from langchain_core.prompts.prompt import PromptTemplate
from langchain.llms import CTransformers


# Fuction to get response from lama2 model

def getLLamaresponse(input_text,no_words,blog_style):

    ## LLAMA model 7b
    llm=CTransformers(model='model/llama-2-7b-chat.ggmlv3.q2_K.bin',
                      model_type="llama",
                      config={"max_new_tokens":256,
                              "temperature":0.01})
        ## Promt templet
    template = f"Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words"

    prompt = PromptTemplate(input_variables=["style","text","n_words"],
                              template=template)
    print(blog_style)
    ## Generate the response from LLAMA 2 Model
    response = llm(prompt.format(style=blog_style,text=input_text,n_words=no_words))
    print(response)
    return response




st.set_page_config(page_title="Generate Blogs",
                    page_icon = "🤖",
                    layout= 'centered',
                    initial_sidebar_state = "collapsed")

st.header("Generate Blogs 🤖")


input_text = st.text_input("Enter the BLog Topic")


## creating two more columns for additional 2 fields

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of words")
with col2:
    blog_style = st.selectbox("writing the blog for",
                        ("Reserchers", "Data scientist","common people"),index=0)


submit = st.button("Generate")

## Final Response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))
