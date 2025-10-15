import pprint


class Map:
    def __init__(self, map_id, name):
        self._id = map_id
        self.name = name
        self.terrain_chunks = {}
        self.terrain_map = []
        self.entity_chunks = {}
        self.entity_map = []
        self.chunk_quantity = 0
        self.width = 6
        self.height = 6
        self.chunk_size = 3

    def load_map_data(self):
        self.terrain_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.entity_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.width = len(self.terrain_map[0])
        self.height = len(self.terrain_map)

    def create_chunks(self):
        self.chunk_quantity = int(self.width / self.chunk_size)
        for y in range(self.chunk_quantity):
            for x in range(self.chunk_quantity):
                terrain_chunk = Chunk(x, y, self.chunk_size, self.terrain_map)
                entity_chunk = Chunk(x, y, self.chunk_size, self.entity_map)
                self.terrain_chunks[terrain_chunk._id] = terrain_chunk.loaded_chunk
                self.entity_chunks[entity_chunk._id] = entity_chunk.loaded_chunk

    def get_chunk(self, x, y):
        chunk_x = int(x / self.chunk_size)
        chunk_y = int(y / self.chunk_size)
        return (chunk_x, chunk_y)

    def get_pos(self, x, y):
        pos_x = int(x % self.chunk_size)
        pos_y = int(y % self.chunk_size)
        return (pos_x, pos_y)


class Chunk:
    def __init__(self, x, y, size, map_object):
        self._id = f"{x}x{y}"
        self.loaded_chunk = []
        for y_index in range(size):
            chunk_line = []
            for x_index in range(size):
                chunk_line.append(map_object[y * size + y_index][x * size + x_index])
            self.loaded_chunk.append(chunk_line)
