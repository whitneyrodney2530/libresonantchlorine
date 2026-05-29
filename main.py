"""mediator_3c2941 - State machine."""
from enum import Enum, auto
import json
MACHINE_ID = "mediator_3c2941"
class State(Enum):
    IDLE = auto()
    RUNNING = auto()
    PAUSED = auto()
    DONE = auto()
    ERROR = auto()
TRANSITIONS = {State.IDLE: [State.RUNNING], State.RUNNING: [State.PAUSED, State.DONE, State.ERROR], State.PAUSED: [State.RUNNING, State.IDLE], State.DONE: [State.IDLE], State.ERROR: [State.IDLE]}
class Machine:
    def __init__(self): self.state = State.IDLE; self.history = []
    def transition(self, target: State) -> bool:
        if target in TRANSITIONS.get(self.state, []):
            self.history.append({"from": self.state.name, "to": target.name})
            self.state = target; return True
        return False
    def status(self) -> dict: return {"machine": MACHINE_ID, "state": self.state.name, "steps": len(self.history)}
def main():
    m = Machine()
    for s in [State.RUNNING, State.PAUSED, State.RUNNING, State.DONE, State.IDLE]: m.transition(s)
    print(f"[{MACHINE_ID}] {json.dumps(m.status(), indent=2)}")
    print(f"[{MACHINE_ID}] History: {json.dumps(m.history, indent=2)}")
if __name__ == "__main__":
    main()
