import numpy as np
import onnxruntime as ort
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model',default='mobilenet-13.onnx' , type=str)
args = parser.parse_args()
onnx_model = args.model

img = np.array((1,3,640,640)).astype(np.float32)
  
sess_ort = ort.InferenceSession(onnx_model)

sess_ort.get_modelmeta()
first_input_name = sess_ort.get_inputs()[0].name
first_output_name = sess_ort.get_outputs()[0].name

print(first_input_name, first_output_name)

res = sess_ort.run(None, {first_input_name: img})
print("the expected result is \"7\"")
print("the digit is classified as \"%s\" in ONNXRruntime"%np.argmax(res))
