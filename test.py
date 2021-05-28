from src.core.types.variable import Variable

age = Variable(name='age', value=14)

if __name__ == '__main__':
    age.set_value(15)
    print(age.to_dict())