from game.Background import Background
from game.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position= (0, 0)):
        match entity_name:
            case 'LvL1':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'LvL1BG{i}', (0,0)))
                    list_bg.append(Background(f'LvL1BG{i}', (WIN_WIDTH,0)))
                return list_bg