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
        kiwis=[("A",) for _ in range(self.num_kiwis)],
        dogs=[("E",) for _ in range(self.num_dogs)]
        ) # TODO: Ask Edu if this is valid

    def is_valid_state(self, _):
        True # Asegurem que sigui valid des de les accions


    # TODO: Trobar manera de referenciar el cost de graph, he posat A i B com a exemple del que vull fer
    # Movem tots els dogs disponibles, del primer punt possible al segon punt possible, cost definit per graph dinamicament
    @action(DDRange(0, 'num_dogs'), Categorical(["A", "B", "C", "D", "E", "F", "G"]), cost=1)
    def moveDog(self, state, dog_id, dog_to):
        
        dog_from = state.dogs[dog_id]
        
        # Asegurem de que existeix la aresta
        try:
            if self.graph[dog_from, dog_to] is not None:
                cond = self.graph[dog_from, dog_to][1] # somebody(C)
                
                #Comprovem que hi ha algú al node que hi ha dins del sombody(X)
                if "somebody" in cond and (cond[-2:-1] in state.kiwis or cond[-2:-1] in state.dogs):
                    # Recordem que no podem modificar una tupla
                    new_dogs = list(state.dogs)
                    new_dogs[dog_id] = dog_to
                    return State(kiwis=state.kiwis, dogs=tuple(new_dogs))
                
                if "nobody" in cond and (cond[-2:-1] not in state.kiwis or cond[-2:-1] not in state.dogs):
                    new_dogs = list(state.dogs)
                    new_dogs[dog_id] = dog_to
                    return State(kiwis=state.kiwis, dogs=tuple(new_dogs))
                
        except KeyError:
            return None

    # Movem tots els kiwis disponibles, del primer punt possible al segon punt possible, cost definit per graph dinamicament
    @action(DDRange(0, 'num_kiwis'), Categorical(["A", "B", "C", "D", "E", "F", "G"]), cost=1)
    def moveKiwi(self, state, kiwi_id, kiwi_to):
        
        kiwi_from = state.kiwis[kiwi_id]
        
        try:
            # Asegurem de que existeix la aresta
            if self.graph[kiwi_from, kiwi_to] is not None:
                cond = self.graph[(kiwi_from, kiwi_to)][1] # somebody(C)
                
                #Comprovem que hi ha algú al node que hi ha dins del sombody(X)
                if "somebody" in cond and (cond[-2:-1] in state.kiwis or cond[-2:-1] in state.dogs):
                    new_kiwis = list(state.kiwis)
                    new_kiwis[kiwi_id] = kiwi_to
                    return State(kiwis=tuple(new_kiwis), dogs=state.dogs)
                
                if "nobody" in cond and (cond[-2:-1] not in state.kiwis or cond[-2:-1] not in state.dogs):
                    new_kiwis = list(state.kiwis)
                    new_kiwis[kiwi_id] = kiwi_to
                    return State(kiwis=tuple(new_kiwis), dogs=state.dogs)

                return None
            
        except KeyError:
            return None