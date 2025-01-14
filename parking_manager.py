class ParkingSpace:
    def __init__(self, id, coordinates):
        self.id = id
        self.coordinates = coordinates
        self.is_occupied = False

class ParkingManager:
    def __init__(self):
        self.spaces = {}

    def add_space(self, id, coordinates):
        self.spaces[id] = ParkingSpace(id, coordinates)

    def update_spaces(self, detections):
        for space in self.spaces.values():
            space.is_occupied = self.is_space_occupied(space.coordinates, detections)

    def is_space_occupied(self, space_coords, detections):
        for det in detections:
            x1, y1, x2, y2, conf, cls = det
            if self.calculate_overlap(space_coords, (x1, y1, x2, y2)) > 0.5:
                return True
        return False

    def calculate_overlap(self, rect1, rect2):
        x1 = max(rect1[0], rect2[0])
        y1 = max(rect1[1], rect2[1])
        x2 = min(rect1[2], rect2[2])
        y2 = min(rect1[3], rect2[3])

        intersection = max(0, x2 - x1) * max(0, y2 - y1)
        area1 = (rect1[2] - rect1[0]) * (rect1[3] - rect1[1])
        area2 = (rect2[2] - rect2[0]) * (rect2[3] - rect2[1])

        return intersection / (area1 + area2 - intersection)

    def get_available_spaces(self):
        return sum(1 for space in self.spaces.values() if not space.is_occupied)

    def get_occupied_spaces(self):
        return sum(1 for space in self.spaces.values() if space.is_occupied)

