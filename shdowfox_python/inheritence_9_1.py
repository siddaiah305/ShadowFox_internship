class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        return f"Calling {number}..."

    def receive_call(self):
        return "Incoming call..."

    def take_a_picture(self, camera_type="rear"):
        if camera_type == "front":
            return f"Taking a selfie with {self.front_camera}MP front camera."
        return f"Taking a picture with {self.rear_camera}MP rear camera."

    def get_specs(self):
        return f"Screen: {self.screen_type}, Network: {self.network_type}, Dual SIM: {self.dual_sim}, Front Camera: {self.front_camera}MP, Rear Camera: {self.rear_camera}MP, RAM: {self.ram}GB, Storage: {self.storage}GB"


class Apple(MobilePhone):
    def __init__(self, model, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "5G", False, front_camera, rear_camera, ram, storage)
        self.model = model

    def get_specs(self):
        return f"Apple {self.model} - " + super().get_specs()


class Samsung(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "5G", dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def get_specs(self):
        return f"Samsung {self.model} - " + super().get_specs()


iphone1 = Apple("iPhone 14 Pro", 12, 48, 6, 128)
iphone2 = Apple("iPhone 13", 12, 12, 4, 64)

galaxy1 = Samsung("Galaxy S22", True, 16, 108, 8, 256)
galaxy2 = Samsung("Galaxy A52", True, 8, 64, 6, 128)

print(iphone1.get_specs())
print(iphone1.make_call("9876543210"))
print(iphone1.take_a_picture("front"))

print(galaxy1.get_specs())
print(galaxy1.receive_call())
print(galaxy1.take_a_picture())
