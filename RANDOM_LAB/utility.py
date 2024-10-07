import random

class MarbleBag:
    def __init__(self, o_bag) -> None:
      self.bag = []
      self.o_bag = o_bag

    def draw(self):
        if not self.bag:
         self.bag = self.o_bag.copy()
         random.shuffle(self.bag)
        return self.bag.pop() 


class ProgressiveProb():
    def __init__(self, success_rate, increment) -> None:
        self.base_success_rate = success_rate
        self.current_success_rate = self.base_success_rate
        self.increment = increment
    
    def reset_probability(self):
        self.current_success_rate = self.base_success_rate

    def attempt(self):
        p = random.uniform(0, 100)
        if p < self.current_success_rate:
            print(f"successful {self.current_success_rate}")
            self.reset_probability()
            return True
        else:
            self.current_success_rate = self.current_success_rate + self.increment
            print(f"failed {self.current_success_rate}")
            return False
        

class FixedLimit():
    def __init__(self, probability, fixed_success_rate) -> None:
        self.attempt_count = 0
        self.fixed_success_rate = fixed_success_rate
        self.base_probability = probability
    
    def attempt(self):
        self.attempt_count = self.attempt_count + 1
        if self.attempt_count >= self.fixed_success_rate:
            self.attempt_count = 0
            return True
        roll = random.uniform(0, 100)
        if roll < self.base_probability:
            self.attempt_count = 0
            return True
        else:
            return False        
        

class Predetermination():
    def __init__(self, max_attempts) -> None:
        self.attempts = 0
        self.success_at = random.randint(1, max_attempts)
        self.max_attempts = max_attempts
    
    def attempt(self):
        self.attempts = self.attempts + 1
        if self.attempts >= self.success_at:
            self.attempts = 0
            return True
        else:
            return False                      