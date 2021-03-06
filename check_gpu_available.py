import tensorflow as tf
#
# gpus = tf.config.list_physical_devices(device_type="GPU")
# tf.config.set_visible_devices(devices=gpus[0], device_type="GPU")
# tf.config.experimental.set_memory_growth(device=gpus[0], enable=True)
#
# print(tf.config.list_physical_devices('GPU'))
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

import torch
# print(torch.zeros(1).cuda())
# print(torch.device("cuda"))
print(torch.__version__)         
print(torch.version.cuda)           
print(torch.cuda.is_available())
