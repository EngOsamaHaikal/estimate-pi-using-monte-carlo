

import random
import math 
import matplotlib.pyplot as plt 
import matplotlib.patches as pat 


def estimatePI():
 status=True 
 while status : 
  j=input("Enter the number of points here : ")
  points_within=0
  total_points=0
  Xpoints=list()
  Ypoints=list()

  for i in range(int(j)):

    x_axis=random.uniform(0,1)
    y_axis=random.uniform(0,1)
    d=x_axis**2+y_axis**2

    Xpoints.append(x_axis)
    Ypoints.append(y_axis)

    if d<=1:
      points_within+=1

    total_points+=1    

  pi=4*points_within/total_points
  exact_pi=math.pi
  print("\n A plot of the points in/out the circle :\n")
  c=pat.Circle((0.5,0.5),radius=0.5,fill=False)

  ax=plt.axes()
  ax.add_patch(c)
  
  plt.scatter(Xpoints,Ypoints,s=1)
  plt.axis([0, 1, 0, 1])

  plt.show()

  percentagte_of_error=abs(((exact_pi-pi)/exact_pi))
  print("\nFinal output is : ")
  print( pi ,"and Percentage Of error = "+str(percentagte_of_error)) 
  print("\nDo you want to exit or change the number of points\n")
  userChoice = input("Enter exit  or change\n ")
  if userChoice=="exit" :
    status=False 
  elif userChoice=="change":
    continue

estimatePI()

