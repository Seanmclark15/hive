__author__ = "Zack Snyder"
__date__ = "1/23/19"

# import unique identifier library
from uuid import uuid4

class Group():
    """Group class desribing logical grouping of nodes in network"""

    def __init__(self, id=None, controller=None, distances=dict(), max_size=0):
        """Initialize Group class

        * addresses: list of node addresses in group
        """
        # Set an unique id for the group
        if id is not None:
            self.id = id
        else:
            self.id = uuid4()
        
        self.controller = controller
        # Dictionary of address: distance key-value pairs
        self.distances = dict(distances)
        # Address of all nodes in group
        self.addresses = [address for address, _ in sorted(self.distances.items(), lambda kv: kv[1])]
        # Distances between current node and other nodes
        # self.distances = [distance for address, distance in self.nodes]
        # Maximum size of a group
        self.max_size = max_size

    def merge(self, source, address, group):
        """Merge two groups together"""
        if source in group.addresses[:self.max_size + 1]:
            if address not in self.addresses: 
                self.addresses.append(address)
            if len(group.nodes) < self.max_size:
                self.max_size = len(group.addresses)
        elif address in self.addresses:
            self.addresses.remove(address)
        # Reduce size of group to max size
        self.addresses = self.addresses[:self.max_size]

    def add(self, address, distance):
        """Add an address to the group"""
        self.distances[address] = distance

    def remove(self, address):
        """Remove an address from the group"""
        if address in self.distances: del self.distances[address]
        if address in self.addresses: self.addresses.remove(address)
