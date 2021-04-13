import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = ["numpy",
                "Pillow",
                "torch",
                "torchvision",
                "tqdn",
                "easydict",
                "opencv-python"]

setuptools.setup(
    name="arcface_torch",
    version="0.1.0",
    description="A PyTorch re-implementation of ArcFace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomasic/arcface_torch",
    package_data={
        "": ["*.txt", "*.rst", "*.pth", "*.npy", "*.log"],
    }
)
