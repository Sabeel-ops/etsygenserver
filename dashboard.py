import tkinter as tk
import random
import time

class CarDashboard:
    def __init__(self, master):
        self.master = master
        master.title("Digital Car Dashboard")
        master.geometry("600x400")
        master.configure(bg='black')

        # Speed Display
        self.speed_var = tk.StringVar()
        self.speed_label = tk.Label(
            master, 
            textvariable=self.speed_var, 
            font=('Digital-7', 72), 
            fg='green', 
            bg='black'
        )
        self.speed_label.pack(pady=20)

        # RPM Display
        self.rpm_var = tk.StringVar()
        self.rpm_label = tk.Label(
            master, 
            textvariable=self.rpm_var, 
            font=('Digital-7', 36), 
            fg='green', 
            bg='black'
        )
        self.rpm_label.pack()

        # Additional Gauges Frame
        gauge_frame = tk.Frame(master, bg='black')
        gauge_frame.pack(pady=20)

        # Fuel Level
        self.fuel_var = tk.StringVar()
        self.fuel_label = tk.Label(
            gauge_frame, 
            textvariable=self.fuel_var, 
            font=('Arial', 18), 
            fg='green', 
            bg='black'
        )
        self.fuel_label.grid(row=0, column=0, padx=20)

        # Engine Temperature
        self.temp_var = tk.StringVar()
        self.temp_label = tk.Label(
            gauge_frame, 
            textvariable=self.temp_var, 
            font=('Arial', 18), 
            fg='green', 
            bg='black'
        )
        self.temp_label.grid(row=0, column=1, padx=20)

        # Warning Area
        self.warning_var = tk.StringVar()
        self.warning_label = tk.Label(
            master, 
            textvariable=self.warning_var, 
            font=('Arial', 16), 
            fg='red', 
            bg='black'
        )
        self.warning_label.pack(pady=10)

        # Start dashboard updates
        self.update_dashboard()

    def update_dashboard(self):
        # Simulate dynamic car data
        speed = random.randint(0, 180)
        rpm = random.randint(0, 6000)
        fuel = random.randint(10, 100)
        temp = random.randint(70, 120)

        # Update speed and RPM
        self.speed_var.set(f"{speed} km/h")
        self.rpm_var.set(f"RPM: {rpm}")

        # Update fuel and temperature
        self.fuel_var.set(f"Fuel: {fuel}%")
        self.temp_var.set(f"Temp: {temp}°C")

        # Warning logic
        warnings = []
        if fuel < 20:
            warnings.append("LOW FUEL")
        if temp > 110:
            warnings.append("OVERHEAT")

        self.warning_var.set(" | ".join(warnings) if warnings else "")

        # Schedule next update
        self.master.after(1000, self.update_dashboard)

def main():
    root = tk.Tk()
    dashboard = CarDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()