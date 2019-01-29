import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import linalg

def read_params():
  x_data = pd.read_csv("linearX.csv",header=None)
  y_data = pd.read_csv("linearY.csv",header=None)
  x = np.asmatrix(np.array(x_data))
  y = np.asmatrix(np.array(y_data))
  x = normalize(x)
  return (x,y)

def normalize(mat):
  mean = np.mean(mat,axis=0)
  var = np.var(mat,axis=0)
  for i in range (len(mat)):
    mat[i,:] = mat[i,:] - mean
    mat[i,:] = mat[i,:]/var
  z = np.zeros((mat.shape[0],1),dtype=float)
  z+=1
  z = np.hstack((z,mat))
  return z

def compute_cost(x,y,theta):
  prod = np.dot(x,theta)
  diff = y-prod
  diff = np.multiply(diff,diff)
  rv = np.sum(diff,axis=0)
  return rv

def gradient(x,y,theta):
  diff = np.dot(x,theta) - y
  grad2 = np.asmatrix(np.zeros((x.shape[0],x.shape[1]),dtype=float))
  for i in range (len(diff)):
    grad2[i,:] = np.multiply(x[i,:],diff[i])
  grad = np.sum(grad2,axis=0).transpose()
  return grad

def algo(x,y,theta,alpha):
  num_iter = 100
  while(num_iter!=0):
    grad = gradient(x,y,theta)
    theta-=alpha*grad
    num_iter-=1
  return

def main():
  (x,y) = read_params()
  theta = np.asmatrix(np.zeros((x.shape[1],1),dtype=float,order='F'))
  alpha = 0.03
  algo(x,y,theta,alpha)

if __name__ == "__main__":
	main()