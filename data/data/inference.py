from doctr.models import recognition
import torch
from doctr.datasets import VOCABS
import doctr.transforms as T
from torchvision.io import read_image

def Predict(img_path, checkpoint_resume, architecture ="crnn_vgg16_bn_diacritics", input_size=32, vocab="diacritics_training"):
    img = read_image(img_path)
    model = recognition.__dict__[architecture](
        pretrained=False,
        input_shape=(3, input_size, 4 * input_size),
        vocab=VOCABS[vocab]).eval()
    if isinstance(checkpoint_resume, str):
        print(f"Resuming {checkpoint_resume}")
        checkpoint = torch.load(checkpoint_resume, map_location="cpu")
        model.load_state_dict(checkpoint)
        preprocess=T.Resize((input_size, input_size*4))
    input_tensor = preprocess(img)
    input_tensor = input_tensor.unsqueeze(0)
    input_tensor =input_tensor.type(torch.float)
    output = model(input_tensor)
    return output

print(Predict("/home/venkat/workspace/sanskritdiacritics-doctr/data/data/inputImgs/img3.jpeg", "/home/venkat/workspace/sanskritdiacritics-doctr/crnn_vgg16_bn_diacritics_20230814-235658_lr_0.00003_IASTandEng.pt"))
