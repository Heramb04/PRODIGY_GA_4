import gradio as gr
import torch
from PIL import Image
from torchvision import transforms
from model import GeneratorUNet
from random_picker import get_random_sample

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load generator
generator = GeneratorUNet()
generator.load_state_dict(torch.load("generator.pth", map_location=device))
generator.to(device)
generator.eval()

# Preprocessing transform
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

# Inference function
def predict(input_image):
    input_tensor = transform(input_image).unsqueeze(0).to(device)
    with torch.no_grad():
        output_tensor = generator(input_tensor).squeeze(0).cpu()
    output_image = transforms.ToPILImage()(output_tensor.clamp(-1, 1) * 0.5 + 0.5)
    return output_image

# Random generation using preloaded samples
def pick_random_and_generate():
    image = get_random_sample()
    return predict(image)

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## 🏗️ Pix2Pix Facade Generator")
    gr.Markdown("Upload a label map or click 'Pick Random' to try a sample!")

    with gr.Row():
        img_input = gr.Image(type="pil", label="Upload Label Map")
        img_output = gr.Image(type="pil", label="Generated Facade")

    with gr.Row():
        btn_run = gr.Button("Generate from Upload")
        btn_random = gr.Button("🎲 Pick Random & Generate")

    btn_run.click(fn=predict, inputs=img_input, outputs=img_output)
    btn_random.click(fn=pick_random_and_generate, inputs=None, outputs=img_output)

demo.launch(share=True)