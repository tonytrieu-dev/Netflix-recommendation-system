from setuptools import setup, find_packages

setup(
    name="netflix-recommender",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
    ],
    author="Tony Trieu",
    description="A Netflix recommendation system that provides personalized movie and TV show suggestions",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        'netflix_recommender': ['*.csv'],
    },
)
