import easyocr

reader = easyocr.Reader(['en'])

def read_text(image):
    results = reader.readtext(image)
    
    texts = []
    for result in results:
        texts.append(result[1])
    
    return texts