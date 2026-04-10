import gradio as gr
from chatbot import chatbot_response

demo = gr.Interface(
    fn=chatbot_response,
    inputs=["number", "number", "number"],
    outputs="text",
    title="AI Customer Retention Assistant"
)

demo.launch()