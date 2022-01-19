import math 

def get_data(file_path):
    result = []
    with open('.txt', 'r') as f:
        for line in f: 
            result.append(list(map(float, line.split(' '))))
    return result 

def analyze_data(result, method):
    number = []
    for i in list: 
        for j in i: 
            number.append(j)
    if method == 'average': 
        mean = ((sum(number)/ len(number))
        print(mean)
    if method == 'standard deviation':
        print(math.sqrt([(x - mean) ** 2 for x in number]/len(number)))
    if method == 'covariance':
        mean_0 = sum(list[0]/len(list[0]))
        mean_1 = sum(list[1]/len(list[1]))
        sub_0 = [i - mean_0 for i in list[0]]
        sub_1 = [i - mean_1 for i in list[1]]
        numerator = sum([sub_0[i]*sub_1[i] for i in range(len(sub_0))])
        denominator = len(list[0])-1
        print(numerator/denominator)
    if method == 'correlation':
        mean_0 = sum(list[0]/len(list[0]))
        mean_1 = sum(list[1]/len(list[1]))
        sub_x = [i - mean_0 for i in mean_0]
        sub_y = [i - mean_1 for i in mean_1]
        numerator = sum([sub_0[i]*sub_1[i] for i in range(len(sub_0))])
        std_deviation_0 = sum([sub_0[i]**2.0 for i in range(len(sub_0))])
        std_deviation_1 = sum([sub_1[i]**2.0 for i in range(len(sub_1))])
        # squaring by 0.5 to find the square root
        denominator = (std_deviation_0*std_deviation_1)**0.5 # short but equivalent to (std_deviation_x**0.5) * (std_deviation_y**0.5)
        cor = numerator/denominator
        print(cor)

result = get_data('.txt')
analyze_data(result,'standard deviation')

#np.correlate(result[0], result[1])
