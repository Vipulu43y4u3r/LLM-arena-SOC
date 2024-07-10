# Streamlit app
st.title("LLM ARENA")

# User input
user_prompt = st.text_area("Enter your prompt:", height=100)

# Model selection
selected_models = st.multiselect(
    "Select models to compare:",
    list(model_functions.keys()),
    default=["Google AI's Gemini", "Anthropic's Claude"]
)

# Generate responses
if st.button("Generate Responses"):
    if user_prompt and selected_models:
        for model_name in selected_models:
            st.subheader(f"{model_name} Response:")
            with st.spinner(f"Generating response from {model_name}..."):
                try:
                    response = model_functions[model_name](user_prompt)
                    st.write(response)
                except Exception as e:
                    st.error(f"Error generating response from {model_name}: {str(e)}")
    else:
        st.warning("Please enter a prompt and select at least one model.")

# Add some information about the app
st.sidebar.title("About LLM ARENA")
st.sidebar.info(
    "This app allows you to compare responses from different language models. "
    "Enter a prompt, select the models you want to compare, and click 'Generate Responses' "
    "to see how each model responds to your input."
)

# Add a footer
st.sidebar.markdown("---")
st.sidebar.markdown("Created with ❤ using Streamlit")

app.py