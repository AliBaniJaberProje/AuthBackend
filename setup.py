from setuptools import setup, find_packages

setup(
    name="auth_backend",
    version="0.1",
    package_dir={"": "src"},  # Tell setuptools your packages are under src/
    packages=find_packages(where="src"),  # Find packages under src/
    install_requires=["bcrypt", "PyJWT", "requests"],
    author="Ali Banijaber",
    description="Reusable JWT-based authentication package with Google and Facebook OAuth support",
    keywords=["authentication", "jwt", "google login", "facebook login"],
)
