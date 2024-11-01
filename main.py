import pandas as pd
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        """
        Initialize a Point with x and y coordinates.

        Parameters:
        - x (float): The x-coordinate of the point.
        - y (float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        """
        Move the point by dx and dy.

        Parameters:
        - dx (float): The change in x-coordinate.
        - dy (float): The change in y-coordinate.
        """
        self.x += dx
        self.y += dy

    def __repr__(self):
        """Return a string representation of the Point."""
        return f"Point({self.x}, {self.y})"


def read_points_from_file(file_path):
    """
    Read points from a text file and return a list of Point objects.

    Parameters:
    - file_path (str): The path to the text file containing the coordinates.

    Returns:
    - List[Point]: A list of Point objects.
    """
    data = pd.read_csv(file_path, header=None, names=['X', 'Y'], delim_whitespace=True)
    return [Point(float(row['X']), float(row['Y'])) for index, row in data.iterrows()]


def plot_points(points, color='blue', label='Original Points'):
    """
    Plot a list of Point objects on a scatter plot.

    Parameters:
    - points (List[Point]): The list of Point objects to plot.
    - color (str): The color of the points.
    - label (str): The label for the points in the legend.
    """
    x_coords = [point.x for point in points]
    y_coords = [point.y for point in points]
    plt.scatter(x_coords, y_coords, color=color, label=label)


def main():
    # Define the path to the coordinates file
    file_path = r"C:\Users\USER\PycharmProjects\Assignment 2\x_y_coordinates.txt"

    # Read points from the file
    points = read_points_from_file(file_path)

    # Plot original points
    plot_points(points, color='blue', label='Original Points')

    # Translate points (for example, move by (1, 1))
    translation_vector = (1, 1)  # Change this to any desired translation
    for point in points:
        point.translate(*translation_vector)

    # Plot translated points
    plot_points(points, color='red', label='Translated Points')

    # Customize plot
    plt.title('Scatter Plot of Points')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.grid(True)
    plt.legend()
    plt.show()


# Run the driver program
if __name__ == "__main__":
    main()