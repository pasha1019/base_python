from faker import Faker


fake_data= Faker('ru_RU')
print(fake_data.name())
print(fake_data.email())
print(fake_data.address())
print(fake_data.job())
