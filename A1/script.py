import numpy as np
import matplotlib.pyplot as plt
print( '---------------' )
box=[25, 11, 40, 17, 17, 41, 21, 31, 46, 26, 86, 74, 100, 28, 15, 97,75,68,82,3];
print( 'box is \n', box)

print( 'count is \n', len(box))


sortBox=np.sort(box )
print('sorted box  is \n', sortBox)

sortBox1=sortBox[0:10]
sortBox2=sortBox[10:]
print('  sortBox1  is \n', sortBox1)
print('  sortBox2  is \n', sortBox2)

print('  sortBox1 median is \n',np.median(sortBox1)  )
print('  sortBox2 median is \n',np.median(sortBox2)  )

sMax=max(sortBox) 
sMin=min(sortBox) 
print('  sortBox max is \n',sMax )
print('  sortBox min is \n',sMin  )
print('  sortBox 3 interval is \n',(sMax-sMin)/3)
print('  sortBox 4 interval is \n',(sMax-sMin)/4)
# print('  sortBox1 mean is \n',np.mean(sortBox1)  )
# print('  sortBox2 mean is \n',np.mean(sortBox2)  )



# res =np.mean(box)
# print( 'mean is ', res)

# res2= np.std(box)
# print( 'standard deviation is ', res2)

# sortArray=np.sort(box )
# print('sorted box  is ', sortArray)

# median=np.median(box)
# print('median is ', median)

# subArray=np.abs( np.subtract(box,median))
# print('subArray is ', subArray)

# sortedSubArray=np.sort(subArray)
# print('sortedSubArray is ', sortedSubArray)

# medianSSA=np.median(sortedSubArray)
# print('medianSSA is ', medianSSA)


# values, counts = np.unique(box, return_counts=True)
# print(values,counts)