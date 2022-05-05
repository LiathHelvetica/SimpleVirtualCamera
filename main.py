from entity_reader import read_assets
from visualisation.main_window import MainWindow
from pyglet.app import run

read_assets()

main_window = MainWindow()
run()
