import turtle
import pandas


class StateInput:
    """Use this class to show alert on screen"""
    def __init__(self):
        self.answered_states = []
        self.data = pandas.read_csv('50_states.csv')
        self.states_count = len(self.data)

    def showAlert(self):
        while len(self.answered_states) < self.states_count:
            window_title = 'Guess the state'
            if len(self.answered_states) > 0:
                window_title = '{0}/{1} states correct'.format(len(self.answered_states), self.states_count)

            answer_state = turtle.textinput(title=window_title,
                                            prompt="What's another state's name?").title()
            if answer_state == 'Exit':
                self.generate_report()
                break

            if answer_state not in self.answered_states and self.validate_and_draw_state(answer_state):
                self.answered_states.append(answer_state)
            else:
                print("Entered state {0} is not valid".format(answer_state))

    def validate_and_draw_state(self, state_name):
        if state_name in self.data.state.to_list():
            state_data = self.data[self.data.state == state_name]
            print("coordinate for {0}: ({1}, {2})".format(state_name, float(state_data.x), float(state_data.y)))
            state_view = turtle.Turtle()
            state_view.hideturtle()
            state_view.penup()
            state_view.goto(float(state_data.x), float(state_data.y))
            state_view.write(state_data.state.item())
            return True
        else:
            return False

    def generate_report(self):
        not_answered_states = [state for state in self.data.state.to_list() if state not in self.answered_states]
        data = {
            'states': not_answered_states
        }

        dataframe = pandas.DataFrame(data)
        file_name = 'states_to_learn.csv'
        dataframe.to_csv(file_name)
        print(not_answered_states)
        print('report generated successfully and saved in {0}.'.format(file_name))
