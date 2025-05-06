from setuptools import setup, find_packages

setup(
    name="polygons_api",
    version="0.1.0",
    description="Библиотека для генерации, преобразования и анализа 2D-многоугольников",
    author="Артём",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "matplotlib>=3.5",
        "shapely>=2.0",
    ],
    python_requires=">=3.8",
)