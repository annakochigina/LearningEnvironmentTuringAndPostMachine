
class ObjPostAlg():
    def __init__(self, infnity_tape, frame_infinity_tape, output_elm_ids, text_task_condition, frame_table_rules, button_right, button_left, button_run=None, button_step=None):
        self.infinity_tape = infnity_tape
        self.frame_infinity_tape = frame_infinity_tape
        self.output_elm_ids = output_elm_ids
        self.text_task_condition = text_task_condition
        self.frame_table_rules = frame_table_rules
        self.button_run = button_run
        self.button_step = button_step

        self.list_label_ind = []
        self.last_save_output_elm = None
        self.last_save_inf_tape = infnity_tape

        self.start_output_elm = None
        self.start_inf_tape = infnity_tape

        self.lst_var = []
        self.button_right = button_right
        self.button_left = button_left
        self.list_answer_stud = []
        self.list_true_answer = []
        self.entry_answer_stud_third = None
        self.var = None

    def hide_right_elm_post(self):
        self.infinity_tape[self.output_elm_ids[1]].option_menu.place(x=-1000, y=-1000)

    def hide_left_elm_post(self):
        self.infinity_tape[self.output_elm_ids[0]].option_menu.place(x=-1000, y=-1000)