# coding=utf-8
"""
1. dict复制: new_dict=dict(old_dict)
"""

# data
dict_demo = dict(a=1, b=2, c=3)

dict_new = dict(dict_demo)
dict_new['d'] = 4

# iterate
print('---iterate')
print("***old:")
for k, v in dict_demo.items():
    print('%s: %s' % (k, v))
print('***new:')
for k, v in dict_new.items():
    print('%s: %s' % (k, v))

# keys
print("---keys")
for k in dict_demo.keys():
    print('key:', k)

# values
print("---values")
for v in dict_demo.values():
    print('value:', v)

print("---length of dict %s: %s" % (dict_demo, len(dict_demo)))

print("---convert %s 2 str: %s" % (dict_demo, str(dict_demo)))

# from keys
ks = ['k' + str(i) for i in range(0, 10)]
dv = -1
dict_fks = dict.fromkeys(ks, dv)
print("dict init from keys %s: %s" % (ks, dict_fks))

# get with default value
k = 'd'
dv = -1
print("value of key '%s' in %s: %s" % (k, dict_demo, dict_demo.get(k, dv)))

# key in dict
k = 'c'
print("is key '%s' in %s: %s" % (k, dict_demo, k in dict_demo))

# set default value -- add k-v if not exists before
k_ext = 'a'
k_notext = 'k_NEW'
print("BEFORE set-default of '%s': %s" % (k_ext, dict_demo.get(k_ext)))
dict_demo.setdefault(k_ext, 'A')
print("AFTER set-default of '%s': %s" % (k_ext, dict_demo.get(k_ext)))
print("BEFORE set-default of '%s': %s" % (k_notext, dict_demo.get(k_notext)))
dict_demo.setdefault(k_notext, 'v_NEW')
print("AFTER set-default of '%s': %s" % (k_notext, dict_demo.get(k_notext)))

# update dict
dict_old = dict(a='a', b='b', c='c')
dict_new = dict(a='A', b='B', k_new='v_new')
print("dict BEFORE update:", dict_old)
dict_old.update(dict_new)
print("dict updated:", dict_old)

# pop -- delete by key
dict4pop = dict.fromkeys([f'k{i}' for i in range(0, 10)], -1)
kpop = 'k5'
print("dict BEFORE pop key '%s': %s" % (kpop, dict4pop))
dict4pop.pop(kpop)
print("dict popped key '%s': %s" % (kpop, dict4pop))

# bulk-generation of dict
print("---generate dict")
bulk_d = {f"k{i}": i for i in range(10)}
for k in bulk_d:
    print(f"{k}:{bulk_d[k]}")