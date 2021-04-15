import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = ["numpy",
                "Pillow",
                "torch",
                "torchvision",
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
        "": ["*.txt", "*.rst", "*.pth",  "data/facebank/*.*", "mtcnn_pytorch/src/weights/*.*", "*.npy", "*.log", "work_space/save/*.pth"],
    },
    package_dir={"": "."},
    packages=setuptools.find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
