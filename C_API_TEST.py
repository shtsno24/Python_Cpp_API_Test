import ctypes

# load .so file
libc = ctypes.cdll.LoadLibrary("./MAC_VEC.so")

# define params and src/dst data
len_vec = 8
coef = 1.1
vec_x = [i * coef for i in range(len_vec)]
vec_a = [2 * coef for i in range(len_vec)]
vec_b = [(i - 16) * coef for i in range(len_vec)]
vec_y = [0 for i in range(len_vec)]

# define data type and convert method
len_vec_type = ctypes.c_uint32
data_type = ctypes.c_float
vec_type = data_type * len_vec

# convert list-type data
_len_vec = len_vec_type(len_vec)
_vec_x = vec_type(*vec_x)
_vec_a = vec_type(*vec_a)
_vec_b = vec_type(*vec_b)
_vec_y = vec_type(*vec_y)

# execution
libc.MAC_VEC_FP32(_len_vec, _vec_a, _vec_x, _vec_b, _vec_y)

# convert results to list-type
result = list(_vec_y)
print(result)

# convert src/dst data from fp32 to int
vec_x = [int(i) for i in vec_x]
vec_a = [int(i) for i in vec_a]
vec_b = [int(i) for i in vec_b]
vec_y = [int(i) for i in vec_y]

# define data type and convert method
data_type = ctypes.c_int16
vec_type = data_type * len_vec

# convert list-type data
_vec_x = vec_type(*vec_x)
_vec_a = vec_type(*vec_a)
_vec_b = vec_type(*vec_b)
_vec_y = vec_type(*vec_y)

# execution
libc.MAC_VEC_INT16(_len_vec, _vec_a, _vec_x, _vec_b, _vec_y)

# convert results to list-type
result = list(_vec_y)
print(result)

# define data type and convert method
data_type = ctypes.c_uint32
vec_type = data_type * len_vec

# convert list-type data
_vec_x = vec_type(*vec_x)
_vec_a = vec_type(*vec_a)
_vec_b = vec_type(*vec_b)
_vec_y = vec_type(*vec_y)

# execution
libc.MAC_VEC_UINT32(_len_vec, _vec_a, _vec_x, _vec_b, _vec_y)

# convert results to list-type
result = list(_vec_y)
print(result)
