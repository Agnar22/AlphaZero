import math
import time
import random
import numpy as np
# from Othello import Gamelogic
from FourInARow import Gamelogic
#import loss
import collections

C_PUCT = sqrt(2)

# OBS: when the game is over it the algorithm expects that it is none to move
class Node:
    def __init__(self, parent, action, t=0, n=0):
        self.parent = parent
        if parent:
            parent.add_child(self)
        self.t = t
        self.n = n
        self.last_action = action
        if parent:
            self.board_state = parent.get_board_state.execute_move(action)
        self.children = []
    
    def get_parent(self):
        return self.parent
    
    def add_child(self, child):
        self.children.append(child)
    
    def is_leaf_node(self):
        if len(children) == 0:
            return True
        return False
    
    def get_board_state(self):
        return self.state
    
    def get_last_action(self):
        return self.last_action
    
    def get_times_visited(self):
        return self.n
    
    def get_total_values(self):
        return self.t

class MCTS:
    
    def __init__(self, tree, start_state, game):
        self.tree = Node(None, None)
        self.tree.board_state = start_state
        self.start_state = start_state
        self.game = game

    def reset_search(self):
        self.tree = Node(None, None)
        self.tree.board_state = self.start_state

    # Setting the game the MCTS will be used on
    def set_game(self, game):
        pas

    # Setting the evaluation algorithm used by the MCTS
    def set_evaluation(self, eval):
        pass

    # Returning a dictionary with action as key and visit number as value
    def get_action_numbers(self, state):
        action_numbers = {}
        node = state
        for child in node.children:
            action_numbers[child.last_action] = child.get_times_visited()



    # Returning the prior probabilities of a state, also known as the "raw" NN predictions
    def get_prior_probabilities(self, state):
        pass

    # Returning the posterior search probabilities of the search,
    # meaning that the percentages is calculated by: num_exec/total
    def get_posterior_probabilities(self, state):
        pass

    # Returning the temperature probabilities calculated from the number of searches for each action
    def get_temperature_probabilities(self, state):
        pass

    # Returning a random move proportional to the temperature probabilities
    def get_temperature_move(self, state):
        pass

    def get_most_searched_move(self, state):
        actions = get_action_numbers(state)
        most_searched_move = 0
        max = -1
        for action in actions:
            if actions[action] > max:
                most_searched_move = action
                max = actions[action]
        return most_searched_move

    # Executing MCTS search a "number" times
    def search_series(self, number):
        for _ in range(number):
            search()

    # Executing a single MCTS search: Selection-Evaluation-Expansion-Backward pass
    def search(self):
        node = self.tree
        self.best_child = None
        while not node.is_leaf_node():
            best_puct = 0
            for n in node.children:
                curr_puct = PUCT(n.state, n.action)
                if (curr_puct > best_puct):
                    best_child = n
                    best_puct = curr_puct
            node = best_child
        node.t = get_info_from_NN(node.state)

    def back_propagate(self, node):
        if node.parent != None:
            node.get_parent.t += node.t
            back_propagate(node.get_parent)



    def PUCT(self, state, action):
        actions = get_action_numbers(state)

        action_state = None
        for child in state.children:
            if child.get_last_action() == action:
                action_state = child


        N = actions[action]
        sum_N_potential_actions = sum(actions.values())
        U = C_PUCT * get_prior_probabilities(state)*math.sqrt(sum_N_potential_actions)/(1+N)

        Q = action_state.get_total_values()/N

        return Q + U
