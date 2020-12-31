height = float(input('请输入您的身高(kg)'))
weight = float(input('请输入您的体重(kg)'))
BMI = weight / height ** 2
if 18.5 < BMI < 24.9:
    print('您的身高体重正常')
elif BMI < 18.5:
    print('您太瘦了')
else:
    print('您太胖了')
