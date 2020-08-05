from setuptools import setup

try:
    # 3.8+
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

__version__ = version(__package__)

with open('README.md', 'r') as f:
      long_description = f.read()

setup(
    name = "docx2pdf",
    version = __version__,
    description = "Convert docx to pdf on Windows or macOS directly using Microsoft Word (must be installed).",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license = "MIT",
    py_modules = [ 'docx2pdf', ],
    entry_points = {
        'console_scripts': ['docx2pdf=docx2pdf:cli'],
    },
    homepage = "https://github.com/AlJohri/docx2pdf",
    repository = "https://github.com/AlJohri/docx2pdf",
    authors = [ "Al Johri <al.johri@gmail.com>" ],
    classifiers = [
        "Operating System :: MacOS",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires='>=3.5',
    install_requires = [
        'tqdm>=4.41.0',
        'pywin32>=227 ; platform_system=="Windows"',
        'appscript>=1.1.0 ; sys_platform=="darwin"',
        'importlib-metadata>=1.1.0 ; python_version<"3.8"',
    ],
    extras_require = {
        'dev': ['pytest>=5.2'],
    },
)
