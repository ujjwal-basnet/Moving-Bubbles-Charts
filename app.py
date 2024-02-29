import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from d3blocks import D3Blocks

# Function to generate random datetime within a range
def random_datetime(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# Generate  100 sample data for moving bubbles
num_samples = 40
num_states_per_sample =100
states = ['Eating', 'Sleeping', 'Home', 'Working', 'Traveling']
state_probabilities = [0.3, 0.3, 0.1, 0.1, 0.2]  # Adjust probabilities for each state
#tried with random datasets but didinot work as expected thus giving proabability 

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

data = []
for sample_id in range(1, num_samples + 1):
    state_changes = [start_date]
    for i in range(num_states_per_sample):
        state_changes.append(random_datetime(state_changes[-1], end_date))
    state_changes = sorted(state_changes)
    for i in range(num_states_per_sample):
        state = np.random.choice(states, p=state_probabilities)
        data.append([state_changes[i+1], state, sample_id])


df = pd.DataFrame(data, columns=['datetime', 'state', 'sample_id'])

# Import library
from d3blocks import D3Blocks

# Initialize D3Blocks
d3 = D3Blocks()

# Specify the sample id with the size of the node (smaller size)
size = {sample_id: random.randint(5, 20) for sample_id in range(1, num_samples + 1)}

# Specify the sample id with the color of the node
color = {sample_id: '#{:06x}'.format(random.randint(0, 0xFFFFFF)) for sample_id in range(1, num_samples + 1)}

# Make the moving bubbles
d3.movingbubbles(df, 
                 datetime='datetime',
                 state='state',
                 sample_id='sample_id',
                 size=size,
                 color=color,
                 color_method='node',
                 timedelta='minutes',
                 speed={"slow": 30, "medium": 50, "fast": 10},
                 filepath='/home/ujjwal/movingbubbles.html',
                 cmap='Set2',
                 standardize='samplewise')
