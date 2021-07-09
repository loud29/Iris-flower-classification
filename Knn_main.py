import csv
import random
import math
import operator


#loading into csv file
def load(filename,split,trainset = [],testset = []):
  with open(filename,'r') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    for i in range(len(dataset)-1):
      for j in range(4):
        dataset[i][j] = float(dataset[i][j])
      if random.random() < split:
        trainset.append(dataset[i])
      else:
        testset.append(dataset[i])

#trainset= []
#testset = []
#load(r'iris.data',0.67,trainset,testset)
#print('train : ' ,len(trainset))
#print('test : ' ,len(testset))


#euclidian distance
def euclidian(dataset1,dataset2,length):
  distance = 0
  for i in range(length):
    distance += pow((dataset1[i]-dataset2[i]),2)
  return math.sqrt(distance)

dataset1 = [2,2,2,'b']
dataset2 = [4,4,4,'a']
#print('distance : ', euclidian(dataset1,dataset2,3))

#neighbors
#k = number of neighbours
def neighbor(testset,trainset,k):
  distances = []
  length = len(testset)-1
  for i in range(len(trainset)):
    distance = euclidian(trainset[i],testset,length)
    distances.append((trainset[i],distance))
  distances.sort(key = operator.itemgetter(1))
  neighbors = []
  for j in range(k):
    neighbors.append(distances[j][0])
  return neighbors

#trainset = [[2,2,2,'a'],[4,4,4,'b']]
#testset = [5,5,5]
#k = number of neighbours
#k=1
#print('neighbours : ' ,neighbors(testset,trainset,k))


#responses
def responses(neighbors):
  maxvotes = {}
  for i in range(len(neighbors)):
    response = neighbors[i][-1]
    if response in maxvotes:
      maxvotes[response] += 1
    else:
      maxvotes[response] = 1
  sortedvotes = sorted(maxvotes.items(),key = operator.itemgetter(1),reverse = True)
  return sortedvotes[0][0]

#neighbors = [[1,1,1,'a'],[2,2,2,'b'],[3,3,3,'b']]
#print(responses(neighbor))


#accuracy
def accuracy(testsets = [],predictionsets = []):
  x = 0
  for i in range(len(testsets)):
    if testsets[i][-1] == predictionsets[i]:
      x += 1
  return (x / float(len(testsets)))*100
  

#testset = [[1,1,1,1,'a'],[2,2,2,2,'a'],[3,3,3,3,'a']]
#prediction = ['a','a','a']
#print(accuracy(testset,prediction))



#final_function to calculate accuracy of all iris data. 
def main():
  print('Sample : Iris Flower species ')
  trainset = []
  testset = []
  split = 0.67
  load('iris.data',split,trainset,testset)
  print('train set : ',len(trainset))
  print('test set : ',len(testset))

  k = 3
  predictionset = []
  for i in range(len(testset)):
    neighbors = neighbor(testset[i],trainset,k)
    response = responses(neighbors)
    predictionset.append(response)
    print('>>> Prediction : ',response,' Actual : ',testset[i][-1])

  Accuracy = accuracy(testset,predictionset)
  print('Accuracy : ',Accuracy)
main()
end = input('END')
