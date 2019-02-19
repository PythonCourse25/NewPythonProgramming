from statistics import mean
from Scipy import stats
Estimates = [1000,1010,200,250,300,900,700,285,290,1200,245,1500,2000,1900,700,210,240,345,600,650,190,90,85,100,110,950]
Estimates.sort()
Estimates = stats.trim_mean(Estimates, 0.1)
for i in range(len(Estimates)):
    print(Estimates[i])
#trim_value = int(.1* len(Estimates))
#Estimates = Estimates[trim_value:]
#Estimates = Estimates[:len(Estimates)-trim_value]
#mean_value = mean(Estimates)
#print(mean_value)






    
    

