class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label
    
    def get_output(self):
        return self.perform_gate_logic()


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
            return int(input(f"Enter input for Gate {self.get_label()}: "))
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
            return int(input(f"Enter input for pin A of Gate {self.get_label()}: "))
        else:
            return self.pin_a.get_from().get_output()
        
    def get_pin_b(self):
        if self.pin_b is None:
            return int(input(f"Enter input for pin B of Gate {self.get_label()}: "))
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
    g1 = AndGate("G1")
    g2 = AndGate("G2")    
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())

    g5 = NandGate("G5")
    g6 = NandGate("G6")
    g7 = AndGate("G7")
    c4 = Connector(g5, g7)
    c5 = Connector(g6, g7)
    print(g7.get_output())


if __name__ == "__main__":
    main()