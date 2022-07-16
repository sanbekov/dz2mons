from lesson_4.cars.get_car_info import get_car_info
Mers = get_car_info('w210','1800 kg', '184hp', '410nm', '210km/h', 'black')
print(Mers.car_info())
print(Mers.start_engine())
print(Mers.stop_engine())
