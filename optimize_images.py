import os
from PIL import Image

ASSETS_DIR = "./assets"
MAX_WIDTH = 1200  # Максимальная ширина

def optimize_images():
    for filename in os.listdir(ASSETS_DIR):
        file_path = os.path.join(ASSETS_DIR, filename)
        
        # Пропускаем папки
        if not os.path.isfile(file_path):
            continue
            
        # Работаем только с картинками
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                with Image.open(file_path) as img:
                    # Если картинка меньше лимита, не трогаем
                    if img.width <= MAX_WIDTH:
                        print(f"Skipping {filename} (small enough)")
                        continue
                    
                    # Вычисляем новую высоту
                    ratio = (MAX_WIDTH / float(img.width))
                    h_size = int((float(img.height) * float(ratio)))
                    
                    # ИСПРАВЛЕНИЕ: Используем Image.LANCZOS напрямую (работает в твоей версии 9.0.1)
                    img = img.resize((MAX_WIDTH, h_size), Image.LANCZOS)
                    
                    # Сохраняем поверх
                    img.save(file_path, optimize=True, quality=85)
                    print(f"Optimized {filename}: {img.width}x{img.height}")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    optimize_images()
