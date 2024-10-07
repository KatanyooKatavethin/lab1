class Predetermination ():

    def __init__(self, max_attempts) -> None:
        self.attemps -0 
        self.success_at = random.radint(1, max_attempts)
        self.max_attempts = max_attempts

    def attempt(self):
        self.attempt = self.attempt + 1
        if self.attempts >= self.success_at:
            self.attempts -0 
            return True
        return False





class FixedRateProb():
    def__init__(self, probability, fixed_sucess_rate) -> None:
    self.attempt_count = 0
    self.fixed_success_rate = fixed_success_rate
    self.based_probability = probability

