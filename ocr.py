import cv2
import pytesseract


def ocr_core(image):
    text = pytesseract.image_to_string(silent, 'storysquadset')
    return text

img = cv2.imread('/Users/victoriadebebe/Documents/GitHub/Lambda_Labs/story-squad-ds-a/Practice Handwriting NB/MW-tester.jpg')

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresh(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

gray = get_grayscale(img)
thresh = thresh(gray)
silent = remove_noise(thresh)

print(ocr_core(silent))