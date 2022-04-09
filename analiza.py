from cProfile import label
import os
import csv
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

data_folder='.\wysokosci_1'
number_of_points=11
number_of_planes=100
list_of_file=[data_folder+str('\\')+x for x in os.listdir(data_folder) if("spoina" in x)] #get all .csv file
joints ={}
#read all .csv data and save it into dict
for i,x in enumerate(list_of_file):
    with open(x,'r') as csvfile:
        csv_reader=csv.reader(csvfile)
        temp=dict()
        for j,row in enumerate(csv_reader):
            temp[j]=row
        joints[i]=temp

##some variables for plot
x=np.linspace(0,5,11)
x_weld=np.arange(0,100)
x_fit =np.linspace(0,5,500)
results=np.zeros([len(list_of_file),3])


#fitting and ploting
for i in range(len(joints)):
    print("Weld "+str(i+1))
    max_of_joint=np.zeros(len(joints[i]))
    results_folder=data_folder+"\weld_"+str(i+1)
    if os.path.exists(results_folder)==False:
        os.mkdir(results_folder)
    for j in range(len(joints[i])):
        row=[float(x) for x in joints[i][j]]
        
        y_fit=CubicSpline(x,row)
        plt.plot(x,row,'o',label="Measurement data")
        plt.plot(x,y_fit(x),label="Fitted data")
        plt.xlabel("Width [mm]")
        plt.ylabel("Height [mm]")
        plt.grid(True)
        title="Weld "+str(i+1)+" section "+str(j+1)
        plt.title(title)
        plt.legend(loc="lower left")
        # plt.show()
        picture_name=data_folder+"\weld_"+str(i+1)+"\section_"+str(j+1)+".png"
        plt.savefig(picture_name)
        plt.close()
        A_fit=y_fit(x_fit)
        max_of_joint[j]=max(A_fit)

    plt.plot(x_weld,max_of_joint)
    title='Avg: '+str(np.mean(max_of_joint))+', std: '+str(np.std(max_of_joint))
    results[i][0]=i
    results[i][1]=np.mean(max_of_joint)
    results[i][2]=np.std(max_of_joint)
    plt.title(title)
    plt.xlabel("Section number ")
    plt.grid(True)
    plt.ylabel("Height [mm]")
    picture_name=data_folder+"\weld_"+str(i+1)+"\\results.png"
    plt.savefig(picture_name)
    plt.close()
results_name=data_folder+"\\results.csv"
with open(results_name, 'w') as f:
    write=csv.writer(f)
    write.writerow(['Weld','Mean','Std'])
    write.writerows(results)

