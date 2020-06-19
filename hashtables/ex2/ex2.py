#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    source_map = dict()
    for ticket in tickets:
        source_map[ticket.source] = ticket.destination
    route = [None] * length
    route[0] = source_map["NONE"]
    for i in range(1, len(route)):
        route[i] = source_map[route[i-1]]
    return route
