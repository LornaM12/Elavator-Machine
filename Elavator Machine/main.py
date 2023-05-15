import random
import tkinter as tk


class ElevatorApp:
    def __init__(self, master):
        # Define the state transition table
        self.transitions = {
            'A': {0: 'A', 1: 'A', 2: 'A', 3: 'A', 4: 'A', 5: 'A', 6: 'A', 7: 'A', 8: 'A'},
            'B': {0: 'B', 1: None, 2: None, 3: 'B', 4: 'B', 5: 'B', 6: None, 7: None, 8: None},
            'C': {0: 'C', 1: None, 2: None, 3: None, 4: None, 5: 'C', 6: 'C', 7: 'C', 8: 'C'}
        }

        # Define the initial state and current floor
        self.initial_state = random.choice(['A', 'B', 'C'])
        self.initial_floor = random.randint(0, 8)
        self.state = self.initial_state
        self.floor = self.initial_floor

        # Create UI elements
        self.current_floor_label = tk.Label(master, text=f'Current floor: {self.initial_floor}')
        self.current_floor_label.pack()

        self.door_label = tk.Label(master, text='Enter door to use (A/B/C):')
        self.door_label.pack()

        self.door_entry = tk.Entry(master)
        self.door_entry.pack()

        self.floor_label = tk.Label(master, text=f'Enter your destination floor:')
        self.floor_label.pack()

        self.floor_entry = tk.Entry(master)
        self.floor_entry.pack()

        self.submit_button = tk.Button(master, text='Submit', command=self.submit)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text='')
        self.result_label.pack()

    def submit(self):
        # Get user input
        door = self.door_entry.get().upper()
        if door not in ['A', 'B', 'C']:
            self.result_label.config(text='Invalid door selected.')
            return
        next_floor = int(self.floor_entry.get())
        if next_floor not in range(0, 9):
            self.result_label.config(text='Invalid floor selected.')
            return
        if self.transitions[door][next_floor] is None:
            self.result_label.config(text=f'Door {door} cannot be used to access floor {next_floor} from {self.floor} '
                                          f'({self.state}). Please select a valid floor for Door {door}.')

            return

        # Update state and current floor based on input
        self.state = self.transitions[door][next_floor]
        self.floor = next_floor

        # Display message for the selected floor and door
        result_text = f'Going to floor {self.floor} using Door {door}.'
        if self.floor == next_floor:
            result_text += '\nArrived at destination floor.'
        self.result_label.config(text=result_text)

        # Update current floor label
        self.current_floor_label.config(text=f'Current floor: {self.floor}')


# Create the Tkinter root window and start the app
root = tk.Tk()
root.title("JKUAT TOWERS ELEVATOR")
app = ElevatorApp(root)
root.mainloop()
