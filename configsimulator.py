__author__ = 'gkour'
from creatures.human import Human
# from creatures.human2 import Human2
from creatures.humantorchbrain import HumanTorchBrain
# from creatures.zombie import Zombie


class ConfigSimulator:
    CSV_FILE_PATH = './log/output{}.csv'
    CSV_LOGGING = True
    BATCH_SIZE = 10
    UI_UPDATE_INTERVAL = 200  # ms
    RACES = [HumanTorchBrain]