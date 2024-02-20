from pygame import Rect

class Physics:
    def __init__(self) -> None:
        pass

    def collide(self, entity1, entity2) -> bool:
        rect1 = Rect(entity1.x, entity1.y, entity1.width, entity1.height)
        rect2 = Rect(entity2.x, entity2.y, entity2.width, entity2.height)
        return rect1.colliderect(rect2)
    
    def collide_local_to_global(self, localEntity, globalEntity, x_offset, y_offset) -> bool:
        rect1 = Rect(localEntity.x + x_offset, localEntity.y + y_offset, localEntity.width, localEntity.height)
        rect2 = Rect(globalEntity.x, globalEntity.y, globalEntity.width, globalEntity.height)
        return rect1.colliderect(rect2)
    
    def collide_obj(self, x1, y1, w1, h1, x2, y2, w2, h2):
        rect1 = Rect(x1, y1, w1, h1)
        rect2 = Rect(x2, y2, w2, h2)
        return rect1.colliderect(rect2)
    
    def collide_list(self, entity, entity_list) -> list:
        rect1 = Rect(entity.x, entity.y, entity.width, entity.height)
        rect_list = []
        for ent in entity_list:
            rect_list.append(Rect(ent.x, ent.y, ent.width, ent.height))
        return rect1.collidelist(rect_list)