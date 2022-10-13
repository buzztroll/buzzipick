from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()


setup(
    name = 'buzzipicks',
    version = '0.0.1',
    author = 'John Bresnahan',
    author_email = 'buzztroll@gmail.com',
    license = 'I dunno ummm MIT?',
    description = 'Backup your photos to a respberry pi and use it as a photo server',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/buzztroll/buzzipick',
    py_modules = ['buzziphoto',],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        buzz-photoframe=buzziphoto.photoframe:main
        buzz-photoweb=buzziphoto.flaskapp:main
    '''
)
