from setuptools import find_packages, setup


def read_requirements(filename="requirements.txt"):
    "Read the requirements"
    with open(filename) as f:
        return [line.strip() for line in f \
                if line.strip() and \
                line[0].strip() != '#' and \
                not line.startswith('-e ')]


def get_version(filename='jobpost/__init__.py', name='VERSION'):
    "Get the version"
    with open(filename) as f:
        s = f.read()
        d = {}
        exec(s, d)
        return d[name]


setup(
    name='django-dept-job-postings',
    version=get_version(),
    author='Dave Gabrielson',
    author_email='Dave_Gabrielson@UManitoba.CA',
    description='A Django app for posting job opportunities',
    url='',
    license='GNU Lesser General Public License (LGPL) 3.0',
    packages=find_packages(),
    install_requires=read_requirements(),
    zip_safe=False,
    include_package_data=True,
)
