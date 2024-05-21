from PIL import Image, ImageDraw

class Planet:
    def __init__(self, image):
        self.image = image
        self.draw = ImageDraw.Draw(self.image)

    def orbit(self, xywh, fill):
        x, y, w, h = xywh
        color_betta, color_alpha, color_orbit = fill

        # Рисуем орбиту
        orbit_bbox = (x, y, x + w, y + h)
        self.draw.ellipse(orbit_bbox, outline=color_orbit, width=3)

        # Координаты и размеры планеты Бетта
        betta_radius = h // 6
        betta_center = (x + w // 2, y + h // 3)
        betta_bbox = (betta_center[0] - betta_radius, betta_center[1] - betta_radius,
                      betta_center[0] + betta_radius, betta_center[1] + betta_radius)
        self.draw.ellipse(betta_bbox, fill=color_betta)

        # Координаты и размеры планеты Альфа
        alpha_radius = h // 16
        alpha_center = (x + 5 * w // 6, y + 5 * h // 8)
        alpha_bbox = (alpha_center[0] - alpha_radius, alpha_center[1] - alpha_radius,
                      alpha_center[0] + alpha_radius, alpha_center[1] + alpha_radius)
        self.draw.ellipse(alpha_bbox, fill=color_alpha)

# Пример использования:
img = Image.new('RGB', (200, 200), '#000000')
drw = Planet(img)
drw.orbit((20, 40, 160, 120), ('#ffffff', '#dddddd', '#999999'))
img.save('result.png')
