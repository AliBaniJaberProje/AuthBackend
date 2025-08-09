from setuptools import setup, find_packages

setup(
    name="auth-backend",  # Use hyphen if you want
    version="0.1",
    packages=find_packages(),  # No where="src"
    install_requires=["bcrypt", "PyJWT", "requests"],
    author="Ali Banijaber",
    description="Reusable JWT-based authentication package with Google and Facebook OAuth support",
    keywords=["authentication", "jwt", "google login", "facebook login"],
)
