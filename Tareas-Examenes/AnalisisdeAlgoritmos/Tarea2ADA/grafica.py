import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Creamos un array con los círculos
circles = [Circle((0, 0), 1), Circle((2, 0), 1), Circle((1, 1.732), 1), Circle((1, -1.732), 1)]

# Creamos un array con los colores para cada región
colors = ['red', 'blue', 'red', 'blue']

# Creamos la figura y los ejes
fig, ax = plt.subplots()

# Agregamos cada círculo y lo coloreamos con el color correspondiente
for i, circle in enumerate(circles):
    ax.add_patch(circle)
    circle.set_facecolor(colors[i])

# Configuramos los límites de los ejes
ax.set_xlim([-1, 3])
ax.set_ylim([-2, 2])

# Mostramos la figura
plt.show()
