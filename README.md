# 🏗️ Pix2Pix Facade Generator

> A Gradio-powered app that uses a Pix2Pix GAN to translate semantic label maps into photorealistic building facades. Trained from scratch and deployed to Hugging Face Spaces.

---

## 🚀 Demo

🎯 **Try the app here**: [Pix2Pix Facade Generator on Hugging Face](https://huggingface.co/spaces/heramb04/Pix2Pix_Shuffler)

Upload a label map or click **🎲 Pick Random & Generate** to preview results from the training set.

---

## 📷 What It Does

- Translates label maps into facade photos  
- Built using Pix2Pix architecture (U-Net Generator + PatchGAN Discriminator)  
- Trained on 400 images from CMP Facade Dataset  
- Interactive UI via Gradio with manual upload or random generation  

---

## 🧠 Model Architecture

- Generator: U-Net with skip connections  
- Discriminator: PatchGAN (classifies 70×70 patches)  
- Losses: Adversarial (BCE) + L1 Pixel Loss  
- Framework: PyTorch  
- Training: 100 epochs on Colab CPU  

---

## 🗂️ Dataset

- **CMP Facade Dataset**  
  Source: [https://cmp.felk.cvut.cz/~tylecr1/facade](https://cmp.felk.cvut.cz/~tylecr1/facade)  
  - Each image: 256×512 resolution  
    - Left: Semantic label map  
    - Right: Real building facade  
  - Preprocessing: Sliced left half (label map) into `/samples/` folder for backend random generation

---

## 🧪 Sample Workflow

1. **Training** done in Colab with:
   - Custom data loader for image slicing  
   - Generator & Discriminator from scratch  
   - L1 + BCE loss optimization  
   - Generator weights saved as `generator.pth`

2. **Testing** using a separate function for side-by-side inference

3. **Deployment** on Hugging Face with full backend support:
   - `app.py`: Gradio UI  
   - `model.py`: Pix2Pix Generator  
   - `random_picker.py`: Random sample logic  
   - `generator.pth`: Trained weights  
   - `samples/`: 400 pre-sliced label maps

---

## 📁 Project Structure
```
root_folder/ 
├── app.py                 # Gradio UI logic 
├── model.py               # Generator architecture 
├── random_picker.py       # Random label map picker 
├── generator.pth          # Trained generator weights 
├── requirements.txt       # Dependencies for Hugging Face Space 
├── samples/               # Label maps sliced from CMP Facade


---

## 💻 Local Usage

To test it locally:

```bash
git clone https://github.com/heramb04/PRODIGY_GA_4.git
cd root_folder
pip install -r requirements.txt
python app.py

---

## 👨‍💻 Author
Heramb Josh

## 📜 License
This project is MIT licensed. CMP Facade Dataset is used under fair academic usage.

