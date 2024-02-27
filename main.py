import cv2

IMAGE = 'image.jpg'
WATERMARK_TEXT = 'zeydan.net'
FONT_FACE = 1
FONT_SCALE = 3
COLOR = (255,255,255)
TICKNESS = 3
ALPHA = 0.2

space = ''.join([' ' for _ in WATERMARK_TEXT])
WATERMARK_TEXT = WATERMARK_TEXT + space

original_image = cv2.imread(IMAGE)
overlay = original_image.copy()

image_width = original_image.shape[1]
image_height = original_image.shape[0]

text_size = cv2.getTextSize(WATERMARK_TEXT, FONT_FACE, FONT_SCALE, TICKNESS)
text_width = text_size[0][0]
text_height = text_size[0][1]

for h in range(0, image_height, text_height):
    start_from = 0
    if h % (2*text_height) == 0:
        start_from = text_width//2
    for w in range(start_from, image_width, text_width):
        cv2.putText(overlay, WATERMARK_TEXT, (w,h*5), FONT_FACE, FONT_SCALE, COLOR, TICKNESS)

watermarked_image = cv2.addWeighted(overlay, ALPHA, original_image, 1 - ALPHA, 0)

cv2.imshow('Watermarked Image', watermarked_image)
cv2.imwrite(f'Watermarked-{IMAGE}', watermarked_image)
cv2.waitKey(0)