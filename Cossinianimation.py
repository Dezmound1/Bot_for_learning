import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import (
	FigureCanvasTkAgg, NavigationToolbar2Tk)


class KossiniOvalPlotter:
	def __init__(self, a, b, scale, root):
		self.a = a
		self.b = b
		self.scale = scale

		self.root = root
		self.root.title("Kossini Oval Plotter")

		self.fig, (self.ax_decart, self.ax_polar) = plt.subplots(2, 1, figsize=(8, 10))
		self.fig.subplots_adjust(left=0.1, right=0.9, bottom=0.4, top=0.9)

		self.plot_kossini_decart()
		self.plot_kossini_polar()

		self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
		self.canvas.draw()
		self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
		self.toolbar.update()
		self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		self.button_to_polar = tk.Button(self.root, text="Switch to Polar", command=self.switch_to_polar)
		self.button_to_polar.pack(side=tk.LEFT)

		self.button_to_decart = tk.Button(self.root, text="Switch to Decart", command=self.switch_to_decart)
		self.button_to_decart.pack(side=tk.LEFT)

		self.scale_text_label = tk.Label(self.root, text="Scale:")
		self.scale_text_label.pack(side=tk.LEFT)

		self.scale_text_box = tk.Entry(self.root)
		self.scale_text_box.insert(0, str(scale))
		self.scale_text_box.pack(side=tk.LEFT)

		self.scale_text_box.bind("<Return>", self.update_scale)

		self.a_text_label = tk.Label(self.root, text="a:")
		self.a_text_label.pack(side=tk.LEFT)

		self.a_text_box = tk.Entry(self.root)
		self.a_text_box.insert(0, str(a))
		self.a_text_box.pack(side=tk.LEFT)

		self.a_text_box.bind("<Return>", self.update_parameters)

		self.b_text_label = tk.Label(self.root, text="b:")
		self.b_text_label.pack(side=tk.LEFT)

		self.b_text_box = tk.Entry(self.root)
		self.b_text_box.insert(0, str(b))
		self.b_text_box.pack(side=tk.LEFT)

		self.b_text_box.bind("<Return>", self.update_parameters)

		self.animation = FuncAnimation(self.fig, self.update_plots, frames=1000, interval=10, repeat=True)

	def plot_kossini_decart(self):
		theta = np.linspace(0, 2 * np.pi, 1000)
		x = self.scale * np.sqrt(self.a ** 2 + self.b ** 2) * np.cos(theta)
		y_positive = self.scale * np.sqrt(np.abs(self.a ** 2 - self.b ** 2)) * np.sin(theta)
		y_negative = -self.scale * np.sqrt(np.abs(self.a ** 2 - self.b ** 2)) * np.sin(theta)

		self.ax_decart.plot(x, y_positive, color='b')
		self.ax_decart.plot(x, y_negative, color='b')
		self.ax_decart.set_xlabel('X')
		self.ax_decart.set_ylabel('Y')
		self.ax_decart.set_title('Kossini Oval in Decart Coordinates')
		self.ax_decart.grid(True)
		self.ax_decart.set_aspect('equal')

	def plot_kossini_polar(self):
		theta_positive = np.linspace(0, np.pi, 1000)
		theta_negative = np.linspace(-np.pi, 0, 1000)
		r_positive = self.scale * np.sqrt(np.abs(self.a ** 2 * np.cos(2 * theta_positive) + self.b ** 2))
		r_negative = self.scale * np.sqrt(np.abs(self.a ** 2 * np.cos(2 * theta_negative) + self.b ** 2))

		self.ax_polar.plot(theta_positive, r_positive, color='b')
		self.ax_polar.plot(theta_negative, r_negative, color='b')
		self.ax_polar.set_title('Kossini Oval in Polar Coordinates')
		self.ax_polar.grid(True)

	def switch_to_polar(self):
		self.ax_decart.set_visible(False)
		self.ax_polar.set_visible(True)
		self.fig.canvas.draw()

	def switch_to_decart(self):
		self.ax_polar.set_visible(False)
		self.ax_decart.set_visible(True)
		self.fig.canvas.draw()

	def update_scale(self, event):
		self.scale = float(self.scale_text_box.get())
		self.update_plots(0)

	def update_parameters(self, event):
		self.a = float(self.a_text_box.get())
		self.b = float(self.b_text_box.get())
		self.update_plots(0)

	def update_plots(self, frame):
		self.ax_decart.clear()
		self.ax_polar.clear()
		self.plot_kossini_decart()
		self.plot_kossini_polar()

		point_x_decart = self.scale * np.sqrt(self.a ** 2 + self.b ** 2) * np.cos(frame / 10)
		point_y_positive_decart = self.scale * np.sqrt(np.abs(self.a ** 2 - self.b ** 2)) * np.sin(frame / 10)
		point_y_negative_decart = -self.scale * np.sqrt(np.abs(self.a ** 2 - self.b ** 2)) * np.sin(frame / 10)

		self.ax_decart.plot(point_x_decart, point_y_positive_decart, 'ro', markersize=5, color='red')
		self.ax_decart.plot(point_x_decart, point_y_negative_decart, 'ro', markersize=5, color='red')

		point_theta_polar = frame / 10
		point_r_polar = self.scale * np.sqrt(self.a ** 2 * np.cos(2 * point_theta_polar) + self.b ** 2)
		self.ax_polar.polar(point_theta_polar, point_r_polar, 'ro', markersize=5, color='red')

		self.fig.canvas.draw()


# Начальные значения параметров овала
a = 1.7
b = 2
scale = 10

root = tk.Tk()
plotter = KossiniOvalPlotter(a, b, scale, root)
root.mainloop()
