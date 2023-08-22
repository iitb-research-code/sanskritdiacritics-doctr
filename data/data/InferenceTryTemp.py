from PIL import Image
from doctr.models import ocr_predictor
import cv2
from doctr.io import DocumentFile

#reco_arch="crnn_vgg16_bn_diacritics"
model = ocr_predictor( pretrained=True)
# PDF
#doc = read_image(path_to_image)
path="/home/venkat/workspace/sanskritdiacritics-doctr/data/data/inputImgs/CSSVolume1/1_49_a.png"
# Analyze
#pil_img = Image.open("/home/venkat/workspace/sanskritdiacritics-doctr/data/data/inputImgs/CSSVolume1/1_48_a.png", mode="r").convert("RGB")

#imgAsimage = cv2.imread(path)
imgAsimage = DocumentFile.from_images(path)

result = model(imgAsimage)
#result.show(imgAsimage)
print(result)
