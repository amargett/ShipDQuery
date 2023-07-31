import cv2 
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

def find_edges(image_path):
    # Read the image from the provided path
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Canny edge detection to find edges
    edges = cv2.Canny(image, threshold1=50, threshold2=150)

    return edges

def get_edge_coordinates(edges):
    # Find the non-zero (edge) pixels in the edges array
    non_zero_indices = np.transpose(np.nonzero(edges))

    # Convert the indices to tuples
    coordinates = [(x, y) for y, x in non_zero_indices]

    return coordinates

def plot_edges_on_coordinate_frame(image_path, edges, val):
    # Read the original image
    image = cv2.imread(image_path)

    # Get the height and width of the image
    height, width = image.shape[:2]

    # Create a coordinate frame with X and Y axes
    coordinate_frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Plot the edges on the coordinate frame
    coordinate_frame[..., 0] = edges

    # Plot the original image on the coordinate frame
    # coordinate_frame[..., 1] = image[..., 1]
    # coordinate_frame[..., 2] = image[..., 2]

    # Show the resulting plot
    plt.figure(num= val, figsize=(8, 6))
    plt.imshow(cv2.cvtColor(coordinate_frame, cv2.COLOR_BGR2RGB))
    plt.title('Edges Plotted on Coordinate Frame')
    plt.axis('off')
    plt.show()

def process_and_plot_images(image_paths):
    i=0
    for image_path in image_paths:
        i+=1
        print(f"Processing image: {image_path}")
        edges = find_edges(image_path)
        plot_edges_on_coordinate_frame(image_path, edges, i)


if __name__ == "__main__":
    # Replace 'image1.jpg', 'image2.jpg', ..., 'image10.jpg' with the actual paths to your 10 images
    image_paths = [
        '1.png',
        '2.jpg',
        '3.webp',
        '4.webp',
        '5.jpg',
        '6.jpg',
        '7.avif',
        '8.jpg',
        '9.webp',
        '10.png'
  
    ]

    process_and_plot_images(image_paths)