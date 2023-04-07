import streamlit as st

messages = [{"role": "system", "content": "Viva AI "}]


def vivaGPT(Chat):
    import openai
    openai.api_key = "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"
   
    messages.append({"role": "user", "content": Chat})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    vivaGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": vivaGPT_reply})
 
    return vivaGPT_reply


def app():
    st.set_page_config(page_title="Viva AI Assistant", page_icon=":guardsman:", layout="wide")
    st.title("Viva AI Assistant")
    st.write("Crafted with ❤️ by [Dhiraj Chaudhari](https://github.com/dhirajviva14) & [Pragati Bavaskar](https://github.com/pragati14B)")
    st.write("Visit our [College Website](http://www.vivadiploma.org/index.aspx#) for more information about us.")
    
    chat_input = st.text_input("Send a message...")
    
    if st.button("Send"):
        reply = vivaGPT(chat_input)
        st.write(reply)


if __name__ == "__main__":
    app()
