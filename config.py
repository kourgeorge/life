__author__ = 'gkour'


class Config:
    LOG_FILE_PATH = './log/log.csv'
    Batch_SIZE = 10
    UI_UPDATE_INTERVAL = 200 #ms

    class ConfigPhysics:
        SPACE_SIZE = 10
        NUM_FATHERS = 200
        ETERNITY = 100000
        SPACE_SLIPPERY = False
        FOOD_CREATURE_RATIO = 1

    class ConfigBiology:
        RACE_NAME = 'mango'
        BASE_DYING_AGE = 800
        DNA_SIZE = 6
        MOVE_ENERGY = 1
        FIGHT_ENERGY = 5
        INITIAL_ENERGY = 100
        MATE_ENERGY = int(INITIAL_ENERGY / 4)
        MATURITY_AGE = 5 #int(BASE_DYING_AGE / 5)
        BASE_LEARN_FREQ = 20
        BASE_VISION_RANGE = 2
        MEAL_SIZE = 6
        WORK_ENERGY = 3

    class ConfigBrain:
        BASE_GAMMA = 0.9
        BASE_LEARNING_RATE = 1e-4
        BASE_HIDDEN_LAYER_SIZE = 6


