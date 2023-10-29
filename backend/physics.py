from pygame import Rect

class Physics:
    def __init__(self) -> None:
        pass

    def collide(self, entity1, entity2) -> bool:
        rect1 = Rect(entity1.x, entity1.y, entity1.width, entity1.height)
        rect2 = Rect(entity2.x, entity2.y, entity2.width, entity2.height)
        return rect1.colliderect(rect2)
    
    def collide_list(self, rect, rect_list) -> list:
        return []