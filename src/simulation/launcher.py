from simulation.setup import setup
from simulation.world_simulation import Simulation


def main() -> None:
    simulation = Simulation(*setup())

    simulation.main_menu()
