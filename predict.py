import onnxruntime
import PIL.Image as Image
import numpy as np
import cv2 as cv

session = onnxruntime.InferenceSession('model.onnx', None)
input_name = session.get_inputs()[0].name

def predict(img : np.ndarray):
    img = np.array(cv.cvtColor(img,cv.COLOR_BGR2RGB),dtype=np.float32)
    cv.normalize(img, img, 0.0, 1.0, cv.NORM_MINMAX)
    img[:,:,0] = (img[:,:,0]-0.485)/0.299
    img[:,:,1] = (img[:,:,1]-0.456)/0.224
    img[:,:,2] = (img[:,:,2]-0.406)/0.225
    img = np.transpose(img, [2,0,1])
    img = np.expand_dims(img,0)
    o=session.run([],{input_name:img})
    return np.floor(o[0].sum())