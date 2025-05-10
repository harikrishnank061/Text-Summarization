import streamlit as st
import cohere

# Function to summarize text using Cohere API
def summarize_text(api_key, text, model='summarize-xlarge', length='short', format='paragraph', extractiveness='medium'):
    try:
        # Initialize the Cohere client with the provided API key
        co = cohere.Client(api_key)
        
        # Call the summarize method from Cohere API
        response = co.summarize(
            text=text,
            model=model,
            length=length,
            format=format,
            extractiveness=extractiveness
        )
        
        # Return the summary
        return response.summary
    
    except Exception as e:
        # Handle errors and display error messages in the Streamlit app
        st.error(f"Error: {str(e)}")
        return None

# Streamlit app layout
st.set_page_config(page_title="Cohere Text Summarization", page_icon="📝")
st.title("📝 Cohere Text Summarization")
st.markdown("Summarize long pieces of text using the Cohere API.")

# Input API key directly in the app (this is where you enter your API key)
api_key = st.text_input("Enter you API Key", type="password")

# Show a warning if the API key is not provided
if not api_key:
    st.warning("⚠️ Please enter your Cohere API key to proceed.")

# Input fields for the text to summarize
text = st.text_area("Enter the text you want to summarize", height=200)

# Options for summary
length = st.selectbox("Summary Length", ["short", "medium", "long"], index=0)
format = st.selectbox("Summary Format", ["paragraph", "bullets"], index=0)
extractiveness = st.selectbox("Extractiveness", ["low", "medium", "high"], index=1)

# Button to trigger summarization
if st.button("Summarize Text"):
    if api_key and text.strip():
        # Call the summarize_text function and pass the API key
        summary = summarize_text(api_key, text, length=length, format=format, extractiveness=extractiveness)
        if summary:
            st.subheader("Summary:")
            st.write(summary)
    else:
        st.warning("⚠️ Please provide both the API key and the text to summarize.")

st.markdown("---")
st.caption("Powered by Cohere | Built with ❤️ using Streamlit")
