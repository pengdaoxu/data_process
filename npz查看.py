import numpy as np
ac = np.load('D:/lab资料/数据集/Synapse/train_npz/case0007_slice160.npz')
print(ac.files)
print(ac['image'])
print(ac)