#sequential
count = 140
subject = "remote work with pthon"
print('Seminar AMIKOM 2018')
print('=' * 10)
print('jumalah kehadiran = {} dan judul = {}'.format(count,subject))
print('jumalah kehadiran = %s dan judul = %s'%(count,subject))

#subject
print('subject = %s' % subject)

qouta = 160

if count/qouta >= 0.8:
    print('rame')
else:
    print('sepi')


#loop
left_over = qouta - count
print(left_over)

for i in range(0, left_over + 1):
    print('kursi yang tersisa {}'.format(i))