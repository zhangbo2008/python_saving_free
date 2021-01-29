'''
测试资源的析构问题, 看看内存

'''


import gc
mod='9'*99999999

print(1)
mod=''
gc.collect()
print(1)







