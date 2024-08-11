my_dict={'Elena':1987,'Basya':2019, 'Runa':2024}
print(my_dict)
print(my_dict['Elena'])
print(my_dict.get('Egor'))
my_dict.update({'Vadim':2009,
                'Milana':2011})
a=my_dict.pop('Runa')
print(a)
print(my_dict)

my_set={'Husky',2,(1,2,3),True,3.5,2,3.5,'Husky',(1,2,3)}
print(my_set)
my_set.add('Яблоко')
my_set.add(56)
my_set.discard('Husky')
print(my_set)