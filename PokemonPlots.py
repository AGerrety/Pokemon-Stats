import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pokemon = pd.read_csv("Pokemon.csv")
type_count = pd.value_counts(pokemon['Type 1'], sort = True).sort_index()
labels = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fariy', 'Fighting', 'Fire',
         'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic',
         'Rock', 'Steel', 'Water']
sizes = type_count

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = labels, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Number of Pokemon by type 1')
#plt.savefig('pie1.png', bbox_inches='tight')
plt.show()