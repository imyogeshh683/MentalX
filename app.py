import streamlit as st
import requests
import time

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer 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"}

# Function to generate text
def generate_text(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]['generated_text']

# Streamlit app
st.set_page_config(page_title="AI Social Media Content Generator", page_icon="🚀")

# Custom CSS for styling
st.markdown("""
<style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
    }
    .stTextInput input {
        font-size: 16px;
        padding: 10px;
    }
    .stMarkdown {
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.title("🚀 AI Social Media Content Generator")
st.write("Generate captions, hashtags, and post ideas in seconds!")

# User input
prompt = st.text_input("What's your post about? (e.g., 'A new coffee shop opening')")

# Generate button
if st.button("Generate Content"):
    if prompt:
        with st.spinner("Generating content..."):  # Loading spinner
            # Improved prompt
            improved_prompt = f"""
            Generate 5 creative Instagram captions and hashtags for: {prompt}.
            Follow this format:
            1. Caption: [text] Hashtags: [hashtags]
            2. Caption: [text] Hashtags: [hashtags]
            3. Caption: [text] Hashtags: [hashtags]
            4. Caption: [text] Hashtags: [hashtags]
            5. Caption: [text] Hashtags: [hashtags]

            Example:
            1. Caption: "Sip, savor, and enjoy the aroma of our freshly brewed coffee! ☕✨" Hashtags: #CoffeeLovers #NewInTown #CoffeeTime
            """
            output = generate_text(improved_prompt)
            time.sleep(2)  # Simulate delay for better UX
        st.success("Done! Here's your content:")
        st.write(output)
    else:
        st.warning("Please enter a topic!")

# Payment link
st.markdown("---")
st.markdown("### 💰 Upgrade to Premium")
st.markdown("Get unlimited access for just Rs 129/month!")
st.markdown("[Buy Now](your-payment-link)")
platform = st.selectbox("Select Platform", ["Instagram", "Twitter", "LinkedIn"])
prompt = f"Generate 5 {platform} captions and hashtags for: {prompt}"
tone = st.selectbox("Select Tone", ["Funny", "Professional", "Inspirational"])
prompt = f"Generate 5 {tone} {platform} captions and hashtags for: {prompt}"
st.image("social_media_icon.png", width=100)
