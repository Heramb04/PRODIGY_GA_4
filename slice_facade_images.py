import os
from PIL import Image

input_folder = "./facades/test"
output_folder = "./samples"
os.makedirs(output_folder, exist_ok=True)

# Support .jpg and .png just in case
image_files = [f for f in os.listdir(input_folder) if f.endswith((".jpg", ".png"))]

if not image_files:
    print("⚠️ No image files found in:", input_folder)
    exit()

for i, filename in enumerate(sorted(image_files)):
    path = os.path.join(input_folder, filename)

    try:
        img = Image.open(path)
        w, h = img.size

        # Crop left half (label map)
        left_half = img.crop((0, 0, w // 2, h))
        out_name = f"sample_{i+1:03d}.jpg"
        out_path = os.path.join(output_folder, out_name)

        left_half.save(out_path)
        print(f"✅ Saved: {out_name}")
    
    except Exception as e:
        print(f"❌ Failed to process {filename}: {e}")

print(f"\n🎉 Finished slicing. {len(image_files)} attempted → Check '{output_folder}' for results.")