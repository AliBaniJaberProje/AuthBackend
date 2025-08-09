from setuptools import setup, find_packages

setup(
    name="auth-backend",
    version="0.1",
    package_dir={"": "src"},  # Tell setuptools where to find packages
    packages=find_packages(where="src"),
    install_requires=["bcrypt", "PyJWT", "requests"],
    author="Ali Banijaber",
    description="Reusable JWT-based authentication package with Google and Facebook OAuth support",
    keywords=["authentication", "jwt", "google login", "facebook login"],
)
