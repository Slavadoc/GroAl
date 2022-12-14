# градиентный спуск  =  gradient descent page 80 
weight = 0.5
goal_pred = 0.8
input = 0.5

for i in range(20):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    # Чистая ошибка
    directon_and_amount = (pred - goal_pred) * input # Масштабирование, обращение знака и остановка
    weight = weight - directon_and_amount

    print('Error: ',  str(error), ' Prediction: ', str(pred))
# # Метод холодно горячо
# weight = 0.5
# input = 0.5
# goal_prediction = 0.8
# step_amount = 0.001 # Шаг изменения веса в каждой итерации ◄—
#
# for iteration in range(1101): # Повторить обучение много раз, чтобы получить наименьшую ошибкуОсобенности обучения методом «холодно/горячо» 77
#     prediction = input * weight
#     error = (prediction - goal_prediction) ** 2
#     print("Error:" + str(error) + " Prediction:" + str(prediction))
#
#     up_prediction = input * (weight + step_amount) # ◄------ Попробовать увеличить!
#     up_error = (goal_prediction - up_prediction) ** 2
#
#     down_prediction = input * (weight - step_amount) # ◄------ Попробовать уменьшить!
#     down_error = (goal_prediction - down_prediction) ** 2
#
#     if(down_error < up_error):
#         weight = weight - step_amount#  ◄-------- , Е(Ли уменьшение дало лучший | результат, уменьшить!
#     if(down_error > up_error):
#         weight = weight + step_amount # ◄ i Если увеличение дало лучший результат, | увеличить!

# def neural_network(input, weight):
#     prediction = input * weight
#     return prediction
#
# number_of_toes = [8.5]
# win_or_lose_binary = [1]
# input = number_of_toes[0]
# true = win_or_lose_binary[0]
# weight = 0.1
# lr = 0.01
# pred = neural_network(input, weight)
# p_up = neural_network(input, weight)+lr
# p_dn = neural_network(input, weight)-lr
# e_up = (p_up - true) ** 2
# error = (pred - true) ** 2
# e_dn =  (p_dn - true) ** 2
# print('error =', error)
# print('e_up =', e_up)
# print('e_dn = ', e_dn)

#Cреднеквадратичная ошибка градиентный спуск
# knob_weight = 0.5
# input = 0.5
# goal_pred = 0.8
#
# pred = input * knob_weight
#
# error = (pred - goal_pred) ** 2
#
# print(error)

# # Short about numPy
# import numpy as np
#
# a = np.zeros((2,4))
# b = np.zeros((4,3))
# c = a.dot(b)
# print(c)
# print(c.shape)
# e = np.zeros((2,1))
# print('(2,1) =',e)
# f = np.zeros((1,3))
# g = e.dot(f)
# print('(2,1) dot (1,3)', g.shape)
# h = np.zeros((5,4))
# i = np.zeros((5,6))
# j = h.dot(i)
# print(j.shape)
# h = np.zeros((5,4))
# i = np.zeros((5,6))
# j = h.dot(i)
# print(j.shape)
# a = np.array([0,1,2,,]) # vector
# b = np.array([4,5,6,7]) # vector
# c = np.array([[0,1,2,3],
#               [4,5,6,7]])# matrix
# d = np.zeros((2,4))
# print('np.zeros((2,4)) = ',d)
# e = np.random.rand(2,5)
# print('np.random.rand(2,5) = ',e)
# print(e)
# print('a =',a)
# print('a * 0.1 =', a * 0.1)
# print('b =',b)
# print('a * b =', a * b)
# print('a * b * 0.2 =', a * b * 0.2)
# print('c =',c)
# print('c * 0.2 = ', c * 0.2)
# print('a * c = ', a * c)
# print(' a * e = ', a * e)

# # несколько слоев with numPy
# import numpy as np
#
# def neural_network(input,weights):
#     hid = input.dot(weights[0])
#     print(hid)
#     pred = hid.dot(weights[1])
#     return pred
#
# ih_wgt = np.array([
#           [0.1, 0.2, -0.1], # игр
#           [-0.1, 0.1, 0.9], #побед
#           [0.1, 0.4, 0.1]]).T  #болельшиков
# hp_wht = np.array([
#           [0.3, 1.1, -0.3], # травмы
#           [0.1, 0.2, 0.0], #победа
#           [0.0, 1.3, 0.1]]).T  #печаль
# weights = [ ih_wgt, hp_wht]
#
# toes = [8,5, 9.5, 9.9, 9.0]
# wlerc = [0.65, 0.8, 0.8, 0.9]
# nfans = [1.2, 1.3, 0.5, 1.0]
# input = np.array()[toes[0], wlerc[0], nfans[0])
#
# pred = neural_network(input, weights)
# print(pred)
# # несколько слоев
# def neural_network(input, weights):
#
#     hid = vector_mat_mul(input, weights[0])
#     pred = vector_mat_mul(hid, weights[1])
#     return pred
#
# def vector_mat_mul(vector, matrix): #vector = input[3] matrix = weights[3,3]
#     output = [None] * len(vector)
#     for n in range(len(vector)):
#         output[n] = w_sum(vector, matrix[n]) # обнавление нового matrix ...= список веткров
#     return output
#
# def w_sum(a,b):
#     # assert (len(a) == len(b))
#     output = 0
#     for n in range(len(a)):
#         output += (a[n] * b[n])
#     return output
#
# ih_wgt = [[0.1, 0.2, -0.1], # игр
#           [-0.1, 0.1, 0.9], #побед
#           [0.1, 0.4, 0.1]]  #болельшиков
# hp_wht = [[0.3, 1.1, -0.3], # травмы
#           [0.1, 0.2, 0.0], #победа
#           [0.0, 1.3, 0.1]]  #печаль
#
# weights = [ ih_wgt, hp_wht]
#
# toes = [8,5, 9.5, 9.9, 9.0]
# wlerc = [0.65, 0.8, 0.8, 0.9]
# nfans = [1.2, 1.3, 0.5, 1.0]
#
# input = [toes[0], wlerc[0], nfans[0]]
#
# pred = neural_network(input, weights)
# print(pred)

# def neural_network(input, weights): #input[3] weights[3,3]
#     pred = vect_mat_mul(input, weights)
#     return pred
#
# def vect_mat_mul(vector, matrix): #vector = input[3] matrix = weights[3,3]
#     output = [None] * len(vector)
#     for n in range(len(vector)):
#         output[n] = w_sum(vector, matrix[n]) # обнавление нового matrix ...= список веткров
#     return output
#
# def w_sum(a,b):
#     # assert (len(a) == len(b))
#     output = 0
#     for n in range(len(a)):
#         output += (a[n] * b[n])
#     return output
#
# weights = [[0.1, 0.1, -0.3],
#             [0.1, 0.2, 0.0],
#             [0.0, 1.3, 0.1]]
# toes = [8,5, 9.5, 9.9, 9.0]
# wlerc = [0.65, 0.8, 0.8, 0.9]
# nfans = [1.2, 1.3, 0.5, 1.0]
#
# input = [toes[0], wlerc[0], nfans[0]]
# pred = neural_network(input,weights)
# print(pred)

# def neural_network(input, weights):
#     pred = ele_mul(input, weights)
#     return pred
#
# def ele_mul(input, weights):
#     output = [None] * len(weights)
#     for n in range(len(weights)):
#         output[n] = input * weights[n]
#     return output
#
# weights = [0.3, 0.2, 0.9 ]
# wlrec = [0.65, 0.8, 0.8, 0.9 ]
# input = wlrec[0]
#
# pred = neural_network(input, weights)
# print(pred)
# import numpy as np
#
# weights = np.array([0.1, 0.2, 0])
# def neural_network(input, weights):
#     pred = input.dot(weights)
#     return pred
#
# toes = np.array([8.5, 9.5, 9.9, 9.0])
# wlrec = np.array([0.65, 0.8, 0.8, 0.9])
# nfans = np.array([1.2, 1.3, 0.5, 1.0])
#
# input = np.array([toes[0],wlrec[0],nfans[0]])
# pred = neural_network(input, weights)
# print(pred)

# def w_sum(a,b):  numpy dot (dot product) ==  скалярное произведение
#     # assert(len(a == len(b)))
#     output = 0
#     for i in range(len(a)):
#         output += (a[i] * b[i])
#     return output
# mult = elementwise_multiplication(a,b)
# print(mult)
# addi = elementwise_addition(a, b)
# print(addi)
# sum = vector_sum(a)
# print(sum)
# average = vector_average(a)
# print(average)
# def neural_network(input, weights):
#     prediction = w_sum(input,weights)
#     return prediction
#

# weights = [0.1, 0.2, 0]
# toes = [8.5, 9.5, 9.9, 9.0]
# wlrec = [0.65, 0.8, 0.8, 0.9]
# nfans = [1.2, 1.3, 0.5, 1.0]
# input = [toes[0], wlrec[0], nfans[0]]
#
# pred = neural_network(input, weights)
#
# print(pred)
