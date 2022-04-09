from firework import Firework
from charge import Charge


class OldFaithful(Firework):
    def __init__(self, location):
        size = (20, 50)
        charges = [
                (250, Charge(self.charge_location(location, size), (255, 0, 0), 4, 200, 14, 8, 50)),
                (230, Charge(self.charge_location(location, size), (255, 0, 0), 4, 200, 14, 8, 50)),
                (210, Charge(self.charge_location(location, size), (255, 0, 0), 4, 200, 14, 8, 50))
            ]
        super().__init__(location, size, (200, 0, 0), 300, charges, "Old Faithful")
        return


class BlueGoblin(Firework):
    def __init__(self, location):
        size = (25, 50)
        charges = [
                (250, Charge(self.charge_location(location, size), (0, 0, 255), 4, 200, 14, 8, 50)),
                (245, Charge(self.charge_location(location, size), (0, 255, 0), 4, 200, 14, 8, 50)),
                (220, Charge(self.charge_location(location, size), (0, 0, 255), 4, 200, 14, 8, 50)),
                (215, Charge(self.charge_location(location, size), (0, 255, 0), 4, 200, 14, 8, 50))
            ]
        super().__init__(location, size, (0, 0, 200), 300, charges, "Blue Goblin")
        return

class RingOfFire(Firework):
    def __init__(self, location):
        size = (10, 60)
        charges = [
                (250, Charge(self.charge_location(location, size), (250, 25, 0), 8, 400, 14, 8, 75)),
                (240, Charge(self.charge_location(location, size), (250, 75, 0), 8, 400, 14, 8, 75)),
                (230, Charge(self.charge_location(location, size), (250, 125, 0), 8, 400, 14, 8, 75)),
                (220, Charge(self.charge_location(location, size), (250, 175, 0), 8, 400, 14, 8, 75)),
                (210, Charge(self.charge_location(location, size), (250, 225, 0), 8, 400, 14, 8, 75))
            ]
        super().__init__(location, size, (250, 125, 0), 300, charges, "Ring of Fire")
        return
