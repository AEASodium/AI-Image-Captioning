import gradio as gr
from transformers import pipeline
import os

# 1. Initialize the Image Captioning Pipeline
# We use the BLIP model (Bootstrapped Language-Image Pre-training) 
# which is lightweight and fits well in the 2GB memory you allocated.
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

def caption_image(image):
    try:
        # Perform inference
        result = captioner(image)
        # Extract the caption text
        return result[0]['generated_text']
    except Exception as e:
        return f"Error processing image: {str(e)}"

# 2. Define the Gradio Interface
demo = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="pil", label="Upload an Image"),
    outputs=gr.Textbox(label="Generated Caption"),
    title="AI Image Captioning Engine",
    description="Upload an image and let the BLIP AI model describe it for you.",
    allow_flagging="never"
)

# 3. Launch the app
# IMPORTANT: Code Engine expects the app to listen on all interfaces (0.0.0.0) 
# and the port we specified (7860)
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)