from doctr.io import DocumentFile
from doctr.models import ocr_predictor

#DET_CKPT = "/home/venkat/workspace/sanskritdiacritics-doctr/crnn_vgg16_bn_diacritics_20230808-161524.pt"
REC_CKPT = "/home/venkat/workspace/sanskritdiacritics-doctr/crnn_vgg16_bn_diacritics_20230808-161524.pt"

model = ocr_predictor(reco_arch='crnn_vgg16_bn',pretrained=True)
#model.det_predictor.model.load_weights(DET_CKPT)
#model.det_predictor.model.postprocessor.unclip_ratio = 2
model.reco_predictor.model.load_weights(REC_CKPT)

if __name__ == "__main__":
    # Image loading
    doc = DocumentFile.from_images("/home/venkat/workspace/sanskritdiacritics-doctr/nav_test/AirConservation.pdf")
    # Models inference
    result = model(doc)
    # Max proba post processing rule for selecting the right VIN value among docTR results
    vin = ""
    for word in result.pages[0].blocks[0].lines[0].words:
        if word.confidence > confidence:
            vin = word.value
            confidence = word.confidence
    # Display the detection and recognition results on the image
    result.show(doc)
