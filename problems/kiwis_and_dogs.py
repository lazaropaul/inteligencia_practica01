from dataclasses import dataclass

from hlogedu.search.problem import Problem, action, Categorical, DDRange


@dataclass(frozen=True, order=True)
class State:
    kiwis: tuple[str]
    dogs: tuple[str]


# Problem
##############################################################################


class KiwisAndDogsProblem(Problem):
    NAME = "kiwis-and-dogs"

    def __init__(self):
        super().__init__()
        # Assume we only have `nobody(X)` and `somebody(X)` conditions.
        # In case of having more than one condition, these will always be
        # a conjunction and will be separated by a comma.
        self.graph = {
            # A
            ("A", "B"): (3, "nobody(E)"),
            ("A", "C"): (4, ""),
            # B
            ("B", "A"): (3, "nobody(E)"),
            ("B", "C"): (1, ""),
            ("B", "G"): (5, ""),
            # C
            ("C", "B"): (1, ""),
            ("C", "D"): (2, "somebody(E),somebody(G)"),
            # D
            ("D", "C"): (2, "somebody(E),somebody(G)"),
            ("D", "E"): (8, "somebody(A)"),
            ("D", "F"): (3, "somebody(C)"),
            # E
            ("E", "D"): (8, "somebody(A)"),
            ("E", "F"): (5, ""),
            # F
            ("F", "D"): (3, "somebody(C)"),
            # G
            ("G", "F"): (7, ""),
            ("G", "B"): (5, ""),
        }
        self.num_kiwis = 2
        self.num_dogs = 1

    def get_start_states(self):
        return [State(kiwis=("D", "F"), dogs=("C",))]

    def is_goal_state(self, state):
        return state == State(
        kiwis=tuple("A" for _ in range(self.num_kiwis)),
        dogs=tuple("E" for _ in range(self.num_dogs))
        )

    def is_valid_state(self, _):
        return True # Asegurem que sigui valid des de les accions
    
    def parseCondition(self, condition):
        if "," in condition:
            return condition.split(",")
        return [condition]


    # TODO: Juntar les 2 actions per evitar repetir codi
    @action(DDRange(0, 'num_dogs'), Categorical(["A", "B", "C", "D", "E", "F", "G"]))
    def moveDog(self, state, dog_id, dog_to):
        
        dog_from = state.dogs[dog_id]
        
        # Asegurem de que existeix la aresta
        try:
            #("4", somebody(X))
            cost = self.graph[(dog_from, dog_to)][0] 
            condition = self.graph[dog_from, dog_to][1]
            
            if condition != "": # Per optimitzar i no haver de pasar pels if's
                condition = self.parseCondition(self.graph[dog_from, dog_to][1]) # separem les condicions en una llista
                
                for i in range(len(condition)): # Comprovem totes les condicions
                    at_node = condition[i][-2:-1]
                    # Si la condició == somebody, comprovem que no hi hagi cap kiwi ni cap gos en el node de la condició ja que si no hi ha ningú, no podem moure, contraexemple aproach
                    if "somebody" in condition[i] and (at_node not in state.kiwis and at_node not in state.dogs):
                        return None
                
                    # Si la condició conté nobody comprovem si hi ha un kiwi o un gos a X, en el cas de que hi hagi, no podem moure 
                    if "nobody" in condition[i] and (at_node in state.kiwis or at_node in state.dogs):
                        return None
                    
                new_dogs = list(state.dogs)
                new_dogs[dog_id] = dog_to
                return (cost, State(kiwis=state.kiwis, dogs=tuple(new_dogs)))
                    
            elif condition == "":
                new_dogs = list(state.dogs)
                new_dogs[dog_id] = dog_to
                return (cost, State(kiwis=state.kiwis, dogs=tuple(new_dogs)))
                
        except KeyError: # En el cas de que no existeixi aresta, ex: (A, A)
            return None

    # Movem tots els kiwis disponibles, del primer punt possible al segon punt possible, cost definit per graph dinamicament
    @action(DDRange(0, 'num_kiwis'), Categorical(["A", "B", "C", "D", "E", "F", "G"]))
    def moveKiwi(self, state, kiwi_id, kiwi_to):
        
        kiwi_from = state.kiwis[kiwi_id]
        
        try:
            # Asegurem de que existeix la aresta
            cost = self.graph[(kiwi_from, kiwi_to)][0]
            condition = self.graph[(kiwi_from, kiwi_to)][1] # somebody(C)
            
            #Comprovem que hi ha algú al node que hi ha dins del sombody(X)
            
            if condition != "":
                condition = self.parseCondition(self.graph[(kiwi_from, kiwi_to)][1])
                
                for i in range(len(condition)):
                    node_at = condition[i][-2:-1]
                    if "somebody" in condition[i] and (node_at not in state.kiwis and node_at not in state.dogs):
                        return None
                    
                    if "nobody" in condition[i] and (node_at in state.kiwis or node_at in state.dogs):
                        return None
                    
                new_kiwis = list(state.kiwis)
                new_kiwis[kiwi_id] = kiwi_to
                return (cost, State(kiwis=tuple(new_kiwis), dogs=state.dogs))
            
            elif condition == "":
                new_kiwis = list(state.kiwis)
                new_kiwis[kiwi_id] = kiwi_to
                return (cost, State(kiwis=tuple(new_kiwis), dogs=state.dogs))
            
        except KeyError:
            return None