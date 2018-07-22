from brain import Brain


class Creature:
    counter = 0
    DNA_SIZE = 5
    INITIAL_ENERGY = 50

    @staticmethod
    def allocate_id():
        Creature.counter += 1
        return Creature.counter

    def __init__(self, universe, dna, id):
        self._id = id
        self._energy = Creature.INITIAL_ENERGY
        self._cell = None
        self._universe = universe
        self._dna = dna
        self._brain = Brain(dna)

    def eat(self):
        self._universe.feed(self)

    def cell(self):
        return self._cell

    def update_cell(self, cell):
        self._cell = cell

    def coord(self):
        return self._cell.get_coord()

    def add_energy(self, amount):
        self._energy += amount

    def move(self, direction):
        self._universe.move_creature(self, direction)

    def id(self):
        return id

    def mate(self):
        self._universe.mate_creature(self)

    def fight(self):
        self._universe.fight(self)

    def dna(self):
        return self._dna

    def internal_state(self):
        return [self._energy]

    def act(self):
        if not self:
            print('stop')
        space_state = self._universe.get_state_in_coord(self.coord())
        state = space_state + self.internal_state()
        decision = self._brain.decide_on_action(state)
        if decision == 0:
            self.move(-1)
        if decision == 1:
            self.move(1)
        if decision == 2:
            self.eat()
        if decision == 3:
            self.mate()
        if decision == 4:
            #self.reduce_energy(1)
            self.fight()

    def energy(self):
        return self._energy

    def reduce_energy(self, amount):
        if self._energy < amount:
            self.die()
            return
        self._energy -= amount

    def die(self):
        self._universe.kill(self)

    def __str__(self):
        return str(self._id)
