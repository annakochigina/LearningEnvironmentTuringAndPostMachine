import processor.turing_machine as turing_machine


class TuringAlg():
    def __init__(self, pointer_index, alphabetical, index_states, counter_states, expression=None):
        self.pointer_index = pointer_index
        self.pointer_value = None
        self.alphabetical = alphabetical
        self.index_states = index_states
        self.expression = expression
        self.counter_elem = len(alphabetical)
        self.counter_states = counter_states

        self.stop_process = False
        self.completed_error = False

        self.start_pointer_index = pointer_index
        self.start_expression = expression

        self.table_rules = {}
        self.last_save_pointer_index = pointer_index
        self.last_save_expression = expression
        self.counter_step = -1
        self.list_entry_states = []
        self.list_entry_alphabet = []
        self.stop_algorithm = False

    def set_expression(self, expression):
        self.expression = expression
        self.pointer_value = self.expression[self.pointer_index]

    def set_val_for_cur_elem(self, new_value, turing_alg_wid):
        self.expression[self.pointer_index] = new_value
        turing_alg_wid.infinity_tape[self.pointer_index].selected_value.set(new_value)

    def move_pointer(self, move_symbol, turing_alg_obj, turing_alg_wid):
        if move_symbol == ">":
            turing_machine.movement_right(turing_alg_obj, turing_alg_wid)
        elif move_symbol == "<":
            turing_machine.movement_left(turing_alg_obj, turing_alg_wid)

        self.pointer_value = self.expression[self.pointer_index]

    def get_current_rule(self):
        return self.table_rules[self.pointer_value][self.index_states - 1].get()

    def color_current_rule(self):
        for key in self.table_rules:
            for cell in self.table_rules[key]:
                cell["background"] = 'white'

        self.table_rules[self.pointer_value][self.index_states - 1]["background"] = 'green'

    def get_alphabetical_str(self):
        str = ""
        for elm in self.alphabetical:
            if elm != " ":
                str += elm

        return str
