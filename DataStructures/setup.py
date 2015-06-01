try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python practice with data structures',
    'author': 'Hayley Anderson',
    'url': 'https://github.com/HayleyCAnderson/PythonPractice.git',
    'download_url': 'https://github.com/HayleyCAnderson/PythonPractice.git',
    'author_email': 'hayleyanderson@zoho.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['stack'],
    'scripts': [],
    'name': 'DataStructures'
}

setup(**config)
