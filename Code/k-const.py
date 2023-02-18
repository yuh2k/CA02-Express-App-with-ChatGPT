# ----------------------------------------------------------------------------------------------------
'''
nim0
Primitive version.
'''
class nim_game0:
    def __init__(self):
        self.states = {"a": 10, "b": 10, "c": 10}
        self.mapping = {
            0: "a",
            1: "b",
            2: "c"
        }

    def console(self):
        import random
        print("Let's play NIM!")
        print("NIM_State", self.states)
        message = ""
        while not set(self.states.values()) == {0}:
            print("your move:")
            input_str = input()
            remove_letter = input_str.split(" ")[0]
            remove_val = int(input_str.split(" ")[1])
            print("removing", remove_val, " from", remove_letter, " gives")
            self.states[remove_letter] -= remove_val
            print("NIM_State",self.states)
            if (set(self.states.values()) == {0}):
                message = "You lose"
                break
            cnt = 0
            # Check if there is only one number that is not 0
            remove_index = random.randint(0, 2)
            while self.states[self.mapping[remove_index]] == 0:
                remove_index = random.randint(0, 2)
            remove_val = random.randint(1, self.states[self.mapping[remove_index]])
            print("computer move: " , self.mapping[remove_index], remove_val)
            print("removing", remove_val, "from", self.mapping[remove_index], "gives")
            self.states[self.mapping[remove_index]] -= remove_val
            print("NIM_State",self.states)
            print("\n")
        if message == "":
            message = "You win"
        print(message)

# if __name__ == "__main__":
#     n0 = nim_game0()
#     n0.console()



# ----------------------------------------------------------------------------------------------------
'''
nim1
    1) Encapsulate computer and user functions. Make the code readble and concise.
    2) Promote mapping, use an array to store the mapping function rather than dictionary.
'''
class nim_game1:
    def __init__(self):
        self.states = {"a": 10, "b": 10, "c": 10}
        self.mapping = ["a", "b", "c"] 

    def computer(self):
        import random
        cnt = 0
        # Check if there is only one number that is not 0
        remove_index = random.randint(0, 2)
        while self.states[self.mapping[remove_index]] == 0:
            remove_index = random.randint(0, 2)
        remove_val = random.randint(1, self.states[self.mapping[remove_index]])
        print("computer move: " , self.mapping[remove_index], remove_val)
        print("removing", remove_val, "from", self.mapping[remove_index], "gives")
        self.states[self.mapping[remove_index]] -= remove_val
    
    def user(self):
        print("your move:")
        input_str = input()
        remove_letter = input_str.split(" ")[0]
        remove_val = int(input_str.split(" ")[1])
        print("removing", remove_val, " from", remove_letter, " gives")
        self.states[remove_letter] -= remove_val

    def console(self):
        print("Let's play NIM!")
        print("NIM_State",self.states)
        
        message = ""
        while not set(self.states.values()) == {0}:
            print("")
            self.user()
            print("NIM_State",self.states)
            print("")
            if set(self.states.values()) == {0}:
                message = "You lose! Computer wins!"
                break
            self.computer()
            print("NIM_State",self.states)
        if message == "":
            message = "You win! Computer loses"

        print(message)
# if __name__ == "__main__":
#     n1 = nim_game1()
#     n1.console()



"""
nim2
    1) Format output, promoted imperfections and fixederrors.
    2) Add is_ended function.
"""

class nim_game1:
    def __init__(self):
        self.states = {"a": 10, "b": 10, "c": 10}
        self.mapping = ["a", "b", "c"] 

    def computer(self):
        import random
        cnt = 0
        # Check if there is only one number that is not 0
        remove_index = random.randint(0, 2)
        while self.states[self.mapping[remove_index]] == 0:
            remove_index = random.randint(0, 2)
        remove_val = random.randint(1, self.states[self.mapping[remove_index]])
        print("computer move:", self.mapping[remove_index], remove_val)
        print("removing", remove_val, "from", self.mapping[remove_index], "gives")
        self.states[self.mapping[remove_index]] -= remove_val
    
    def user(self):
        print("your move:")
        input_str = input()
        remove_letter = input_str.split(" ")[0]
        remove_val = int(input_str.split(" ")[1])
        print("removing", remove_val, "from", remove_letter, "gives")
        self.states[remove_letter] -= remove_val

    def console(self):
        print("Let's play NIM!")
        print("NIM_State",self.states)
        message = ""
        while not set(self.states.values()) == {0}:
            print("")
            self.user()
            print("NIM_State",self.states)
            print("")
            if set(self.states.values()) == {0}:
                message = "You lose! Computer wins!"
                break
            self.computer()
            print("NIM_State",self.states)
        if message == "":
            message = "You win! Computer loses"

        print(message)
if __name__ == "__main__":
    n2 = nim_game1()
    n2.console()
