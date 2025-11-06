class Atom:
    def variables(self, serial, name, residue_name, chain_id, residue_seq, x, y, z, element):
        self.serial = serial
        self.name = name
        self.residue_name = residue_name
        self.chain_id = chain_id
        self.residue_seq = residue_seq
        self.x = x
        self.y = y
        self.z = z
        self.element = element
    def __repr__(self):
        return f"Atom <{self.name} ({self.element}) at ({self.x:.2f},{self.y:.2f},{self.z:.2f})>






        