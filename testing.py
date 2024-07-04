import math


# Assuming you have a class or structure defined for planets, similar to your `Planeta` class

class Planeta:
    def __init__(self, x, y, diametro, color, vel_x, vel_y):
        self.x = x
        self.y = y
        self.diametro = diametro
        self.color = color
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = diametro  # You might use diameter as a proxy for mass in this simulation


def calculate_single_body_acceleration(planetas, body_index):
    G_const = 6.67408e-11  # Gravitational constant in m3 kg-1 s-2
    acceleration_x = 0
    acceleration_y = 0
    target_body = planetas[body_index]

    for index, external_body in enumerate(planetas):
        if index != body_index:
            dx = external_body.x - target_body.x
            dy = external_body.y - target_body.y
            r_squared = dx ** 2 + dy ** 2
            r = math.sqrt(r_squared)

            # Avoid division by zero and handle very close bodies gracefully
            if r_squared > 1e-6:
                acceleration = G_const * external_body.diametro / r_squared
                acceleration_x += acceleration * dx / r
                acceleration_y += acceleration * dy / r

    return acceleration_x, acceleration_y


def actualizar_planetas(planetas, canvas):
    global trazos
    for planeta in planetas:
        # Calculate acceleration
        acc_x, acc_y = calculate_single_body_acceleration(planetas, planetas.index(planeta))

        # Update velocities
        planeta.vel_x += acc_x
        planeta.vel_y += acc_y

        # Update positions
        planeta.x += planeta.vel_x * 0.2  # Adjust 0.2 for your time step
        planeta.y += planeta.vel_y * 0.2  # Adjust 0.2 for your time step

        # Draw the planet
        canvas.crear_ovalo(planeta.x - planeta.diametro / 2, planeta.y - planeta.diametro / 2,
                           planeta.x + planeta.diametro / 2, planeta.y + planeta.diametro / 2,
                           fill=planeta.color, tags="planeta", width=0.5)

        # Optional: Draw trajectory or trail
        canvas.crear_ovalo(planeta.x, planeta.y, planeta.x + 1, planeta.y + 1,
                           fill=planeta.color, width=0, tags="trazo")
        trazos.append("trazo")

    # Remove old traces if necessary
    # eliminar_trazo()

    print(planetas)


def run_simulation(planetas, time_step=0.1, number_of_steps=10000, report_freq=100):
    # Create output container for each body
    body_locations_hist = []
    for current_body in planetas:
        body_locations_hist.append({"x": [], "y": [], "z": [], "name": current_body.name})

    for i in range(1, number_of_steps):
        actualizar_planetas(planetas, canvas)  # Compute gravitational effects and update positions

        if i % report_freq == 0:
            for index, body_location in enumerate(body_locations_hist):
                body_location["x"].append(planetas[index].x)
                body_location["y"].append(planetas[index].y)
                # For 2D simulation, assume z=0
                body_location["z"].append(0)

    return body_locations_hist


def main():
    global canvas
    canvas = Canvas(ANCHO_canvas, ALTURA_canvas)  # PREPARATION
    canvas.configure(cursor="none")
    canvas.establecer_color_fondo_lienzo("gray3")

    # Initialize your planets here with initial positions, velocities, diameters, etc.
    planetas = [
        Planeta(x=700, y=400, diametro=20, color="blue", vel_x=0, vel_y=-2),
        Planeta(x=500, y=400, diametro=15, color="red", vel_x=0, vel_y=2)
        # Add more planets as needed
    ]

    # Run simulation
    simulation_results = run_simulation(planetas)

    # You can access simulation_results to analyze or visualize the history of positions

    canvas.mainloop()


if __name__ == "__main__":
    main()
