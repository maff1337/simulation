from pathlib import Path

from simulation.world import World
from simulation.factory import Factory
from simulation.path_finder import Bfs
from simulation.configs.config import Config
from simulation.actions.make_move import MakeMoveAction
from simulation.renderers.cli_renderer import CliRenderer
from simulation.actions.fill_world import FillWorldAction
from simulation.actions.remove_entities import RemoveEntitiesAction
from simulation.actions.respawn_entities import RespawnEntitesAction
from simulation.actions.refill_actions import RefillActionPointsAction


def setup() -> tuple:
    config_path = Path(__file__).parent / 'configs' / 'config.toml'
    configs = Config(config_path)

    language = 'ru'
    locales_path = Path(configs.get('locales').get(language))

    game_conf_path = Path(configs.get('game').get('game_config'))
    attributes_path = Path(configs.get('game').get('attributes'))

    game_config = Config(game_conf_path)
    locales = Config(locales_path)
    attributes = Config(attributes_path)

    factory = Factory(attributes._config)

    icons = game_config.get('icons')
    coeffs = game_config.get('coeffs')

    world_config = game_config.get('world')

    if not icons or not coeffs or not world_config:
        raise

    rows = world_config.get('rows')
    columns = world_config.get('columns')
    minsize = world_config.get('minsize')

    if not rows or not columns or not minsize:
        raise

    world = World(rows, columns, minsize)

    renderer = CliRenderer(world, icons, locales._config)

    bfs = Bfs()
    fill = FillWorldAction(coeffs, factory)
    make_move = MakeMoveAction(bfs)
    remove = RemoveEntitiesAction()
    refill = RefillActionPointsAction(attributes._config)
    respawn = RespawnEntitesAction(coeffs, factory)

    initial = (fill,)
    turn = (make_move, remove, refill, respawn)

    return initial, turn, world, renderer, language, configs
