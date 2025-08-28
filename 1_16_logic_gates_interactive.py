class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label
    
    def get_output(self):
        return self.perform_gate_logic()
    
    def get_gate_from_user(self):
        gate = int(input("\n1. NOT Gate\n2. AND Gate\n3. OR Gate\n\nEnter gate number based on list (e.g. 1 for NOT Gate): "))
        gate_name = input("Enter gate name: ")
        gate_map = {
            1: NotGate(gate_name),
            2: AndGate(gate_name),
            3: OrGate(gate_name)
        }
        return gate_map[gate]


class Connector:
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate
    
    def get_to(self):
        return self.to_gate


class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.label = label
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            print(f"\nSelect input mode for Gate {self.get_label()}:\n1. Connect a gate\n2. Enter input value")
            input_mode = int(input("Enter your selection (1 or 2): "))
            if input_mode == 1:
                print(f"\nSelect gate for connecting to Gate {self.get_label()}: ")
                gate = self.get_gate_from_user()
                return gate.get_output()
            if input_mode == 2:    
                return int(input(f"\nEnter input for Gate {self.get_label()}: "))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError(f"Input pin not empty for Gate {self.get_label()}")


class BinaryGate(LogicGate):
    def  __init__(self, label):
        super().__init__(label)
        self.label = label
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a is None:
            print(f"\nSelect input mode for pin A of Gate {self.get_label()}:\n1. Connect a gate\n2. Enter input value")
            input_mode = int(input("Enter your selection (1 or 2): "))
            if input_mode == 1:
                print(f"\nSelect gate for connecting to pin A of Gate {self.get_label()}: ")
                gate = self.get_gate_from_user()
                return gate.get_output()
            if input_mode == 2:    
                return int(input(f"\nEnter input for pin A of Gate {self.get_label()}: "))
        else:
            return self.pin_a.get_from().get_output()
        
    def get_pin_b(self):
        if self.pin_b is None:
            print(f"\nSelect input mode for pin B of Gate {self.get_label()}:\n1. Connect a gate\n2. Enter input value")
            input_mode = int(input("Enter your selection (1 or 2): "))
            if input_mode == 1:
                print("\nSelect gate for connecting to pin B of Gate {self.get_label()}: ")
                gate = self.get_gate_from_user()
                return gate.get_output()
            if input_mode == 2:    
                return int(input(f"\nEnter input for pin B of Gate {self.get_label()}: "))
        else:
            return self.pin_b.get_from().get_output()
        
    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        elif self.pin_b is None:
            self.pin_b = source
        else:
            raise RuntimeError(f"No empty input pins in Gate {self.get_label()}")


class NotGate(UnaryGate):
    def __init__(self, label):
        super().__init__(label)
        self.label = label

    def perform_gate_logic(self):
        self.pin = self.get_pin()
        if self.pin:
            return 0
        else:
            return 1


class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)
        self.label = label

    def perform_gate_logic(self):
        self.pin_a = self.get_pin_a()
        self.pin_b = self.get_pin_b()
        if self.pin_a and self.pin_b:
            return 1
        else:
            return 0


class NandGate(AndGate):

    def perform_gate_logic(self):
        if super().perform_gate_logic():
            return 0
        else:
            return 1


class OrGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)
        self.label = label

    def perform_gate_logic(self):
        self.pin_a = self.get_pin_a()
        self.pin_b = self.get_pin_b()
        if self.pin_a or self.pin_b:
            return 1
        else:
            return 0


class NorGate(OrGate):

    def perform_gate_logic(self):
        if self.super().perform_gate_logic():
            return 0
        else:
            return 1


def main():
    logic_gate = LogicGate("dummy")
    build = True
    print("Select output gate: ")
    gate = logic_gate.get_gate_from_user()
    output = gate.get_output()
    print("-"*50)
    print(f"Output: {output}")
    print("-"*50)
        
if __name__ == "__main__":
    main()