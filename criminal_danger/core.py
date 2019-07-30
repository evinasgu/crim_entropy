from collections import defaultdict


class City:
    """
    This class is responsible of represents a graph represented by houses as nodes and streets as edges
    """
    def __init__(self):
        self.city = defaultdict(list)

    def add_street(self, first_house, second_house):
        """
        This method add a street to the city using first_house and second_house as parameters
        :param first_house: represents a house in the city
        :param second_house: represents a house in the city
        """
        self.city[first_house].append(second_house)
        self.city[second_house].append(first_house)

    def execute_generic_bfs(self, first_house, second_house):
        """
        Execute the breath first search algorithm provided for this problem
        :param first_house: represents a house in the city
        :param second_house: represents a house in the city
        :return: A list containing all the data related with the nodes traversed by bfs algorithm
        """
        node_list = []
        visited_keys = self.city.keys()
        visited_values = [False] * len(self.city)
        visited = dict(zip(visited_keys, visited_values))

        queue = []  #Here I am using the initializer [] because is faster than list()
        queue.append(first_house)
        visited[first_house] = True
        while queue:
            first_house = queue.pop(0)
            node_list.append(first_house)
            for i in self.city[first_house]:
                if not visited[i] and i != second_house:
                    queue.append(i)
                    visited[i] = True
        return node_list

    def calculate_danger(self, first_house, second_house):
        """
        Calculate the danger of a street located between first_house and second_house. The trick here is run BFS
        algorithm for first_house ignoring second_house and then run the same algorithm for second_house ignoring
        first_house
        :param first_house: represents a house in the city
        :param second_house: represent a house in the city
        :return:
        """
        first_proliferation = len(self.execute_generic_bfs(first_house, second_house))
        second_proliferation = len(self.execute_generic_bfs(second_house, first_house))
        return first_proliferation * second_proliferation
