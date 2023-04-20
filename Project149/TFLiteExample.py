# Project 149 code from ChatGPT

import gc
import ujson
import ulab
import ulab.numpy as np
import ulab.vector as vector


import tflite_micro as tfl
import model_data
import ulab as np

# Load the model
model = tfl.Model(model_data.model)

# Load the input data
input_data = np.array([[0.1, 0.2, 0.3]])

# Run inference
output_data = model.invoke(input_data)

# Print the result
print(output_data)


