


import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI


# In[11]:


with open("apikey.txt", "r") as f:
    api_key = f.read().strip()

# Configure API key
genai.configure(api_key=api_key)

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)


# In[41]:


def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model name
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"


# In[43]:


# Streamlit UI
st.set_page_config(page_title="AI Data Science Tutor", layout="wide")
st.title("🤖 Data Science Tutor")

st.sidebar.header("Instructions")
st.sidebar.write(
    """
    - Ask any question related to Data Science, ML, AI, Python, etc.
    - Click the *Submit* button or press *Enter* to get a response.
    """
)


# In[45]:


# User input
user_input = st.text_area("Ask a question in Data Science:", "")

if st.button("Submit") and user_input:
    with st.spinner("Thinking... 🤔"):
        response = get_gemini_response(user_input)
    st.success("Response Generated Successfully!")
    st.subheader("AI's Response:")
    st.write(response)


# In[47]:


# Footer
st.sidebar.markdown("---")
st.sidebar.write("Built with ❤️ using Streamlit & Google Gemini API")




# In[ ]:




