import setuptools

setuptools.setup(
    name="hafidzpython",
    version="0.0.1",
    author="Hafidz",
    author_email="hafidz@example.com",
    description="A simple Python package with string and calculator utilities",
    packages=["string", "calculator"],
    python_requires=">=3.10",
    package_dir={"": "src"},
)
