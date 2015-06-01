try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python practice with Five Problems',
    'author': 'Hayley Anderson',
    'url': 'https://github.com/HayleyCAnderson/PythonPractice.git',
    'download_url': 'https://github.com/HayleyCAnderson/PythonPractice.git',
    'author_email': 'hayleyanderson@zoho.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['problem_one', 'problem_two', 'problem_three', 'problem_four'],
    'scripts': [],
    'name': 'FiveProblems'
}

setup(**config)
