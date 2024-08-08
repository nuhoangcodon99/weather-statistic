import pandas as pd
import math
import scipy.stats as stats

df1 = pd.read_excel('hanoi_air_pollution_data_monthly.xlsx', sheet_name='Sheet1', usecols=['Month', 'co'])
df2 = pd.read_excel('hcm_air_pollution_data_monthly.xlsx', sheet_name='Sheet1', usecols=['Month', 'co'])
df3 = pd.read_excel('vn_air_pollution_data_monthly.xlsx', sheet_name='Sheet1', usecols=['Month', 'co'])

# Convert the 'Month' and 'co' columns of the DataFrames to lists
co_values1 = df1['co'].tolist()
co_values2 = df2['co'].tolist()
co_values3 = df3['co'].tolist()

length = len(co_values1)
# Giá trị trung bình mẫu (Mean)
# Hà nội
hnSum = 0
for item in co_values1:
    hnSum = hnSum + item
hnMean = hnSum / length
print('Hanoi Mean: ', hnMean)

# HCM
hcmSum = 0
for item in co_values2:
    hcmSum = hcmSum + item
hcmMean = hcmSum / length
print('Hcm Mean: ', hcmMean)

# Cả nước
vnSum = 0
for item in co_values3:
    vnSum = vnSum + item
vnMean = vnSum / length
print('VN Mean: ', vnMean)

# Độ lệch chuẩn mẫu (Standard deviation)
# Hà nội
hnSDsum = 0
for item in co_values1:
    hnSDsum = hnSDsum + math.pow(item - hnMean, 2)
hnSD = math.pow(hnSDsum/(length - 1), 1/2)
print('Hanoi SD: ', hnSD)

# HCM
hcmSDsum = 0
for item in co_values2:
    hcmSDsum = hcmSDsum + math.pow(item - hcmMean, 2)
hcmSD = math.pow(hcmSDsum/(length - 1), 1/2)
print('Hcm SD: ', hcmSD)

# Cả nước
vnSDsum = 0
for item in co_values3:
    vnSDsum = vnSDsum + math.pow(item - vnMean, 2)
vnSD = math.pow(vnSDsum/(length - 1), 1/2)
print('VN SD: ', vnSD)

#SEM
hnSEM = hnSD / math.pow(length, 1/2)
print('Hanoi SEM: ', hnSEM)
hcmSEM = hcmSD / math.pow(length, 1/2)
print('HCM SEM: ', hcmSEM)
vnSEM = vnSD / math.pow(length, 1/2)
print('VN SEM: ', vnSEM)

# Xác định giá trị t cho khoảng tin cậy 95% và bậc tự do (df)
# Parameters
alpha = 0.025  # significance level
df = length - 1  # degrees of freedom

# Tính giá trị t
t_value = stats.t.ppf(1 - alpha, df)
# Khoảng tin cậy cho
# Hà nội
hnLowerConfidenceValue = hnMean - (t_value * hnSEM)
hnUpperConfidenceValue = hnMean + (t_value * hnSEM)

# HCM
hcmLowerConfidenceValue = hcmMean - (t_value * hcmSEM)
hcmUpperConfidenceValue = hcmMean + (t_value * hcmSEM)

# Cả nước
vnLowerConfidenceValue = vnMean - (t_value * vnSEM)
vnUpperConfidenceValue = vnMean + (t_value * vnSEM)

# Tổng kết lại
print('Khoảng tin cậy 95% với Hà nội: ', '(', hnLowerConfidenceValue, ', ', hnUpperConfidenceValue ,')')
print('Khoảng tin cậy 95% với HCM: ', '(', hcmLowerConfidenceValue, ', ', hcmUpperConfidenceValue ,')')
print('Khoảng tin cậy 95% với Cả nước: ', '(', vnLowerConfidenceValue, ', ', vnUpperConfidenceValue ,')')

#Tính sự khác biệt giữa 2 giá trị trung bình (Mean của hcm và hn)
diffMean = hnMean - hcmMean
print('Difference Mean: ', diffMean)

# Khoảng tin cậy 95% cho sự khác biệt về 2 giá trị trung bình 
diffSEM = math.pow(math.pow(hcmSEM, 2) + math.pow(hnSEM, 2), 1/2)
print('Difference SEM: ', diffSEM)
diffLowerConfidenceValue = diffMean - (t_value * diffSEM)
diffUpperConfidenceValue = diffMean + (t_value * diffSEM)

print('Khoảng tin cậy 95% với Giá trị trung bình giữa HN và HCM: ', '(', 
      diffLowerConfidenceValue, ', ', diffUpperConfidenceValue ,')')
