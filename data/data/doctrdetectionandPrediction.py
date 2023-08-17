from doctr.io import DocumentFile
from doctr.models import detection_predictor,ocr_predictor, linknet_resnet18
from doctr.io import read_img_as_numpy, read_img_as_tensor
from torchvision.transforms.v2 import Compose

from doctr.models import recognition
import torch
from doctr.datasets import VOCABS
import doctr.transforms as T
from torchvision.io import read_image

import cv2

import math
import os



def ScanPage(path):
    doc = read_img_as_numpy(path)
    model = detection_predictor(arch = "db_mobilenet_v3_large", pretrained=True)
    out = model([doc])
    print("out\n",out)
    return out

def convert_coordinates(geometry, page_dim):
    len_x = page_dim[1]
    len_y = page_dim[0]
    x_min = geometry[0]
    y_min = geometry[1]
    x_max = geometry[2]
    y_max = geometry[3]
    x_min = math.floor(x_min * len_x)
    x_max = math.ceil(x_max * len_x)
    y_min = math.floor(y_min * len_y)
    y_max = math.ceil(y_max * len_y)
    return [x_min, x_max, y_min, y_max]



def Predict(img, checkpoint_resume, vocab, architecture ="crnn_vgg16_bn_diacritics", input_size=32):
    # img = torch.from_numpy(img_path)
    img = torch.from_numpy(img.transpose(2, 0, 1))
    model = recognition.__dict__[architecture](
        pretrained=False,
        input_shape=(3, input_size, 4 * input_size),
        vocab=vocab).eval()
    if isinstance(checkpoint_resume, str):
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        checkpoint = torch.load(checkpoint_resume, map_location=device)
        model.load_state_dict(checkpoint)
        preprocess=T.Resize((input_size, input_size*4))
        img_transforms=Compose(
                [
                    T.Resize((input_size, 4 * input_size), preserve_aspect_ratio=True),
                    # Ensure we have a 90% split of white-background images
                    T.ColorInversion()
                ]
            )
    input_tensor = img_transforms(img)
    input_tensor = input_tensor.unsqueeze(0)
    input_tensor =input_tensor.type(torch.float)
    output = model(input_tensor)
    return output["preds"][0][0]

image_folder = "/home/venkat/workspace/sanskritdiacritics-doctr/data/data/inputImgs/CSSVolume1/"
target_folder = "/home/venkat/workspace/sanskritdiacritics-doctr/data/data/inputImgs/CSSVolume1/results/"
checkpoint_path = "/home/venkat/workspace/sanskritdiacritics-doctr/crnn_vgg16_bn_diacritics_20230815-145907_0.00003_IASTandEng_v1.pt"
images = os.listdir(image_folder)
images = sorted(images)

for image in images[2:6]:
    path = os.path.join(image_folder, image)
    img = read_img_as_numpy(path)
    imgAsimage = cv2.imread(path)
    words=ScanPage(path)[0]["words"]
    os.mkdir(os.path.join(target_folder, image))
    counter=0
    output_txt=""
    coords_all=[]
    for word in words:
        print("word in for loop",type(word), word)
        coords = convert_coordinates(word, img.shape)
        print("coords in for loop",type(coords), coords)
        coords_all.append(coords)
        print("coords all",type(coords_all), coords_all)

        local_image = img[int(coords[2]):int(coords[3]), int(coords[0]): int(coords[1])]
        cv2.imwrite(os.path.join(target_folder, image, "word"+str(counter)+".png"), local_image)
        counter+=1
        output = Predict(local_image, checkpoint_path, VOCABS["english"]+VOCABS["sanskrit_transliterated"])
        output_txt+=output+"\n"
    coords_all_tuples = [tuple(box) for box in coords_all]
    color = (0, 255, 0) 
    for mbox in coords_all_tuples:
        mx, my, mwidth, mheight = mbox
        #cv2.rectangle(imgAsimage, (mx, my), (mx + mwidth, my + mheight), color, thickness=2)
        cv2.rectangle(imgAsimage, (mx, mheight), (my, mwidth), color, thickness=2)
    moutput_path = os.path.join(target_folder, image, image+"box"+".png")
    cv2.imwrite(moutput_path, imgAsimage)
    f = open(os.path.join(target_folder, image, image+"_output.txt"), "w")
    f.write(output_txt)