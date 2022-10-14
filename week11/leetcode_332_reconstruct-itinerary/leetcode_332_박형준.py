class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []

        def make_path(tickets, new_path, now):
            if len(tickets) == 0:
                result.append(new_path)
                return
            for flight in tickets:
                if flight[0] != now:
                    continue
                tmp_path = new_path[:]
                tmp_path.append(flight[1])
                tmp_tickets = tickets[:]
                tmp_tickets.remove(flight)
                make_path(tmp_tickets, tmp_path, flight[1])
                if len(result):
                    return
        tickets.sort()
        make_path(tickets, ["JFK"], "JFK")
        return result[0]
