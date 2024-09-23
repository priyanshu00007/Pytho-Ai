import streamlit as st
from ai_assistant import AIAssistant
import time
import random

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Initialize the AI Assistant
assistant = AIAssistant()

st.title("AI Assistant Streamlit App")
st.write("Welcome to your AI Assistant! You can ask about the weather, generate images, or have a general conversation.")

# User input
user_input = st.text_input("You:", "", key="input")

if st.button("Send") or (user_input and st.session_state.get("submit")):
    st.session_state.submit = True  # Set the submit state to True
    # Simulate random loading time
    loading_time = random.uniform(10, 15)  # Random time between 1 and 3 seconds
    
    with st.spinner(f"Fetching response... (Estimated time: {loading_time:.2f} seconds)"):  # Show loading animation
        time.sleep(loading_time)  # Simulate delay

        if user_input.lower() == "quit":
            st.write("Goodbye!")
            st.stop()

        elif user_input.lower().startswith("what is the weather in"):
            location = user_input.split("in")[-1].strip()
            response = assistant.get_weather(location)
            st.success(response.get("message", "No response from AI."))
            sources = assistant.get_sources(response)
            if sources:
                st.markdown("**Sources:** " + ", ".join(sources))

        elif user_input.lower().startswith("get image"):
            image_prompt = user_input[len("get image"):].strip()
            images = assistant.get_image(image_prompt)
            if images:
                for image in images:
                    st.image(image.get("url"), caption=image.get("description", "Generated Image"), use_column_width=True)
            else:
                st.warning("No images generated.")

        else:
            response = assistant.message(user_input)
            st.success(response.get("message", "No response from AI."))

        # Append to conversation history
        st.session_state.conversation.append({"user": user_input, "ai": response.get("message", "")})

# Display conversation history
st.markdown("---")
st.header("Conversation History")

for convo in st.session_state.conversation:
    st.markdown(f"**You:** {convo['user']}")
    st.markdown(f"**AI:** {convo['ai']}")

# JavaScript to handle Escape key
st.markdown(
    """
    <script>
    document.onkeydown = function(e) {
        if (e.key === "Escape") {
            window.location.reload();  // Reload the page to stop
        }
    }
    </script>
    """,
    unsafe_allow_html=True
)
