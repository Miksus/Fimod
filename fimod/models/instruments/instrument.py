

class Instrument:

    _map_positions = {
        "short":"short", "write":"short", "sell":"short", 
        "long":"long", "buy":"long"
    }
    
    def __init__(self, position="long"):
        self.position = self._map_positions[position]
    
    @property
    def is_short(self):
        return self.position == "short"
    
    @property
    def is_long(self):
        return self.position == "long"