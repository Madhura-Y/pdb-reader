import re

#class Model:
 #   def __init__(self):
  #      self.id = None
   #     self.chains = {}

    #def set_data(self, line):
     #   if line.startswith("MODEL"):
    #      self.id = int(line.split()[1])

    #def add_chain(self, chain):
     #   self.chains[chain.id] = chain

    #def __repr__(self):
     #   return f"<Model id={self.id}, NumChains={len(self.chains)}>"




import re

class Model:
    def __init__(self):
        self.id = None
        self.chains = {}

    def set_data(self, line):
        if line.startswith("MODEL"):
            self.id = int(line.split()[1])

    def add_chain(self, chain):
        self.chains[chain.id] = chain

    def __iter__(self):
        for chain in self.chains:
            yield chain
        
    def __getitem__ (self,chain_id):
        for chain in self.chains:
            if chain.id == id:
                return chain
            
    def __repr__(self):
        return f"<Model id={self.id}, NumChains={len(self.chains)}>"

