import setuptools

requirements = ["numpy", "Pillow", "torch", "torchvision", "tqdn", "easydict", "opencv-python"]

setuptools.setup(
     package_data={
        "": ["*.txt", "*.rst", "*.pth", "*.npy", "*.log"],
    }
)
