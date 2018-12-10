import csv
import bayespy as bp
import numpy as np
from colorama import init
from colorama import Fore,Back,Style

ageEnum = {'SuperSeniorCitizer':0,'SeniorCitizen':1,'MiddleAged':2,'Youth':3,'Teen':4}
genderEnum = {'Male':0,'Female':1}
familyhistoryEnum = {'Yes':0, 'No':1}
dietEnum = {'High':0, 'Medium':1, 'Low':2}
lifestyleEnum = {'Athlete':0, 'Active':1, 'Moderate':2, 'Sedetary':3}	
cholestrolEnum = {'High':0, 'BorderLine':1, 'Normal':2}
heartdiseaseEnum = {'Yes':0, 'No':1}

with open('heart_disease_data.csv') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    data = []
    for i in dataset:
        data.append([ageEnum[x[0]],genderEnum[x[1]],familyhistoryEnum[x[2]],dietEnum[x[3]],lifestyleEnum[x[4]],cholestrolEnum[x[5]],heartdiseaseEnum[x[6]]])
        
data = np.array(data)
N = len(data)

p_age = bp.nodes.Dirichlet(1.0*np.ones(5))
age = bp.nodes.Categorical(p_age,plates =(N,))
age.observe(data[:,0])

p_gender = bp.nodes.Dirichlet(1.0*np.ones(2))
gender = bp.nodes.Categorical(p_gender, plates=(N,))
gender.observe(data[:,1])

p_familyhistory = bp.nodes.Dirichlet(1.0*np.ones(2))
familyhistory = bp.nodes.Categorical(p_familyhistory, plates=(N,))
familyhistory.observe(data[:,2])

p_diet = bp.nodes.Dirichlet(1.0*np.ones(3))
diet = bp.nodes.Categorical(p_diet, plates=(N,))
diet.observe(data[:,3])

p_lifestyle = bp.nodes.Dirichlet(1.0*np.ones(4))
lifestyle = bp.nodes.Categorical(p_lifestyle, plates=(N,))
lifestyle.observe(data[:,4])

p_cholestrol = bp.nodes.Dirichlet(1.0*np.ones(3))
cholestrol = bp.nodes.Categorical(p_cholesterol, plates=(N,))
cholestrol.observe(data[:,5])

p_heartdisease = bp.nodes.Dirichlet(np.ones(2), plates = (5,2,2,3,4,3))
heartdisease = bp.nodes.MultiMixture([age,gender,familyhistory,diet,lifestyle,cholestrol],bp.nodes.Categorical,p_heartdisease)
heartdisease.observe(data[:,6])
heartdisease.update()

m = 0
while m ==0:
    print("\n")
    res = bp.nodes.MultiMixture([int(input('Enter Age: ' + str(ageEnum))), int(input('Enter Gender: ' + str(genderEnum))), int(input('Enter FamilyHistory: ' + str(familyHistoryEnum))), int(input('Enter dietEnum: ' + str(dietEnum))), int(input('Enter LifeStyle: ' + str(lifeStyleEnum))), int(input('Enter Cholesterol: ' + str(cholesterolEnum)))], bp.nodes.Categorical, p_heartdisease).get_moments()[0][heartDiseaseEnum['Yes']]
    print('Probability(HeartDisease):' +str(res))
    print("enter for continue:0,Exit:1")