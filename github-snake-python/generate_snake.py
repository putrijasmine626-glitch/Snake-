import os
import random
from PIL import Image, ImageDraw

# 1. Konfigurasi Ukuran Gambar (Grid Kotak Kontribusi GitHub)
GRID_SIZE = 15
GAP = 3
COLS, ROWS = 53, 7  # Standar grid kontribusi GitHub (53 minggu x 7 hari)
WIDTH = COLS * (GRID_SIZE + GAP) + GAP
HEIGHT = ROWS * (GRID_SIZE + GAP) + GAP

def create_snake_gif():
    frames = []
    
    # Koordinat awal ular (kepala dan tubuh)
    snake = [[3, 3], [2, 3], [1, 3], [0, 3]]
    # Koordinat makanan awal (kotak hijau terang)
    food = [10, 3]
    
    # Membuat 40 bingkai (frames) animasi bergerak
    for _ in range(40):
        # Membuat latar belakang gambar baru (Warna Gelap/Dark Mode GitHub)
        img = Image.new("RGBA", (WIDTH, HEIGHT), "#0d1117")
        draw = ImageDraw.Draw(img)
        
        # Menggambar Grid Kotak Kontribusi (Latar Belakang)
        for c in range(COLS):
            for r in range(ROWS):
                x1 = c * (GRID_SIZE + GAP) + GAP
                y1 = r * (GRID_SIZE + GAP) + GAP
                x2 = x1 + GRID_SIZE
                y2 = y1 + GRID_SIZE
                draw.rectangle([x1, y1, x2, y2], fill="#161b22")
        
        # Logika Pergerakan Ular Sederhana menuju Makanan
        head = snake[0].copy()
        if head[0] < food[0]: head[0] += 1
        elif head[0] > food[0]: head[0] -= 1
        elif head[1] < food[1]: head[1] += 1
        elif head[1] > food[1]: head[1] -= 1
        
        # Jika ular memakan makanan, ganti posisi makanan secara acak
        if head == food:
            food = [random.randint(0, COLS-1), random.randint(0, ROWS-1)]
        else:
            snake.pop() # Potong ekor jika tidak makan
            
        snake.insert(0, head) # Tambah kepala baru
        
        # Gambar Makanan (Hijau Terang)
        fx = food[0] * (GRID_SIZE + GAP) + GAP
        fy = food[1] * (GRID_SIZE + GAP) + GAP
        draw.rectangle([fx, fy, fx+GRID_SIZE, fy+GRID_SIZE], fill="#39d353")
        
        # Gambar Ular (Warna Hijau Ular GitHub)
        for i, part in enumerate(snake):
            sx = part[0] * (GRID_SIZE + GAP) + GAP
            sy = part[1] * (GRID_SIZE + GAP) + GAP
            color = "#26a641" if i == 0 else "#006d21" # Kepala lebih terang
            draw.rectangle([sx, sy, sx+GRID_SIZE, sy+GRID_SIZE], fill=color)
            
        frames.append(img)
    
    # --- BAGIAN PERBAIKAN UTAMA ---
    # Memanggil fungsi .save() melalui objek elemen pertama di dalam list frames
    os.makedirs("dist", exist_ok=True)
    frames[0].save(
        "dist/python-snake.gif",
        save_all=True,
        append_images=frames[1:],
        optimize=False,
        duration=150, # Kecepatan gerak ular (milidetik)
        loop=0
    )
    print("Animasi Ular Python berhasil dibuat di folder dist/python-snake.gif!")

if __name__ == "__main__":
    create_snake_gif()
