class Car:

    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_enjine(self):
        print(f'Enjine on Title:{self.title}  Model:{self.model} started!')
    def stop_enjine(self):
        print(f'Enjine on Title:{self.title}  Model:{self.model} stoped!')
    def info(self):
        print(f'All info Ttile:{self.title}\nModel:{self.model}\nWeight{self.weight}')
        print(f'Hp:{self.hp}\nNm:{self.nm}\nMax_speed:{self.max_speed}\nColor:{self.color}')

mers = Car('Mersedes', 'Maybach', '2800 kg', '530hp', '1500nm', '350km/h', 'black')
mers.start_enjine()
mers.stop_enjine()
mers.info()

bmw = Car('BMW', 'X3', '1800 kg', '184hp', '410nm', '210km/h', 'red')
bmw.start_enjine()
bmw.stop_enjine()
bmw.info()
