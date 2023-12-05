import processor.turing_machine as turing_machine


class ObjTuringAlg():
    def __init__(self, infnity_tape, frame_infinity_tape, frame_table_rules, output_elm_ids, text_task_condition,
                 button_right, button_left, list_lbl_comments=None, entry_alphabetical=None, button_run=None,
                 button_step=None):
        self.infinity_tape = infnity_tape
        self.frame_infinity_tape = frame_infinity_tape
        self.output_elm_ids = output_elm_ids
        self.list_label_ind = []
        self.list_lbl_comments = list_lbl_comments
        self.text_task_condition = text_task_condition
        self.frame_table_rules = frame_table_rules
        self.entry_alphabetical = entry_alphabetical
        self.button_run = button_run
        self.button_step = button_step
        self.tests = None

        self.last_save_output_elm = None
        self.last_save_inf_tape = infnity_tape

        self.start_output_elm = [-9, 9]
        self.start_inf_tape = infnity_tape

        self.lst_var = []
        self.button_right = button_right
        self.button_left = button_left
        self.list_answer_stud = []
        self.list_true_answer = []
        self.entry_answer_stud_third = None
        self.var = None

    def move_inf_tape(self, move_symbol, turing_alg_obj, turing_alg_wid):
        if move_symbol == "R":
            turing_machine.movement_right(turing_alg_obj, turing_alg_wid)
        elif move_symbol == "L":
            turing_machine.movement_left(turing_alg_obj, turing_alg_wid)

    def hide_right_elm(self):
        self.infinity_tape[self.output_elm_ids[1]].option_menu.place(x=-1000, y=-1000)

    def hide_left_elm(self):
        self.infinity_tape[self.output_elm_ids[0]].option_menu.place(x=-1000, y=-1000)
