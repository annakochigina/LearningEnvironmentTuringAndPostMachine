
class PostAlg():
    def __init__(self, table_rules, alphabetical, pointer_index, alphabet_size, expression=None):
        self.table_rules = table_rules
        self.alphabetical = alphabetical
        self.pointer_index = pointer_index
        self.alphabet_size = alphabet_size
        self.expression = expression

        self.stop_process = False
        self.completed_error = False

        self.start_pointer_index = pointer_index
        self.start_expression = expression

        self.pointer_value = None
        self.number_str = 1
        self.stop_algorithm = False
        self.counter_step = -1
        self.list_number_row = []
        self.list_entry_heading = []
        self.last_save_pointer_index = pointer_index
        self.last_save_expression = expression

    def set_expression(self, expression):
        self.expression = expression
        self.pointer_value = self.expression[self.pointer_index]

    def get_current_command(self):
        return self.table_rules[self.number_str - 1][0].get()

    def get_current_transition(self):
        return self.table_rules[self.number_str - 1][1].get()

    def set_val_for_cur_elem(self, new_value, post_alg_wid):
        self.expression[self.pointer_index] = new_value
        post_alg_wid.infinity_tape[self.pointer_index].selected_value.set(new_value)

    def color_current_command(self):
        for lst in self.table_rules:
            for cell in lst:
                cell["background"] = 'white'

        self.table_rules[self.number_str - 1][0]["background"] = 'green'