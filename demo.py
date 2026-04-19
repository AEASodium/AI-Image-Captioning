import gradio as gr
from transformers import pipeline
import os

# 1. Initialize the Image Captioning Pipeline
# We use the BLIP model (Bootstrapped Language-Image Pre-training) 
# which is lightweight and fits well in the 2GB memory you allocated.
captioner = pipeline("image-text-to-text", model="Salesforce/blip-image-captioning-base")

def caption_image(image):
    try:
        # We pass an empty string as the text input to satisfy the pipeline
        result = captioner(image, "", generate_kwargs={"max_new_tokens": 50}) 
        return result[0]['generated_text']
    except Exception as e:
        return f"Error processing image: {e}"
    
# 2. Define the Gradio I
# nterface
demo = gr.Interface(
    fn=caption_image, 
    inputs=gr.Image(type="pil"), 
    outputs="text",
    title="AI Image Captioning",
    description="Upload an image to get an AI-generated caption.",
    flagging_mode="never"  # Change 'allow_flagging' to 'flagging_mode'
)

# 3. Launch the app
# IMPORTANT: Code Engine expects the app to listen on all interfaces (0.0.0.0) 
# and the port we specified (7860)
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)