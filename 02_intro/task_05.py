'''Опишите декоратор класса, который принимает на вход другой класс
и снабжает декорируемый класс всеми атрибутами входного класса,
названия которых НЕ начинаются с "_". В случае конфликтов имён
импортируемый атрибут должен получить имя с суффиксом "_new".
'''


def copy_class_attrs(cls):
    def decorator(decor_class):
        for item in cls.__dict__.items():  # атрибуты
            if item[0][:1] != '_':  # Проверяем условие

                if item[0] not in decor_class.__dict__:
                    setattr(decor_class, item[0], item[1])
                else:
                    setattr(decor_class, item[0] + '_new', item[1])  # при совпадении добавляем суфикс

            else:
                attr = item[0][len(cls.__name__) + 3:]
                attr_name = ''.join(['_', decor_class.__name__, '_', item[0][len(cls.__name__) + 2:]])
                if attr_name in decor_class.__dict__:
                    attr_name = ''.join([attr_name, '_new'])
                    attr = ''.join([attr, '_new'])
                setattr(decor_class, attr_name, item[1])

                def f(name=item[0]):
                    return getattr(cls, name)

                setattr(decor_class, 'get_' + attr, f)

        return decor_class

    return decorator


class computer:
    _member = ['System', 'Monitor', 'Keybord']
    hdd = '1 Gb'
    _cpu = 3600
    _gpu = 2000
    osu = '16 Gb'
    manufacturer = 'Asus'

    def __init__(self):
        pass


@copy_class_attrs(computer)
class Motherboard:
    _member = ['Mainboard', 'bios', 'sata', 'raid']
    manufacturer = 'Asus'
    _bios = 2010
    _raid = 10
    _gpu = 2000
    hdd = '1 Gb'


for item in Motherboard.__dict__.items():
    print(item)
