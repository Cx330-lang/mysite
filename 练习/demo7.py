import scipy.io
data = scipy.io.loadmat('ice017_p_3of3m.mat')  # 读取mat文件
# print(data.keys())   # 查看mat文件中的所有变量
# print(data['val'])
# # print(data['matrix2'])
# matrix1 = data['val']
# # matrix2 = data['matrix2']
# print(matrix1)
# # print(matrix2)
params = data.values()
print(params)