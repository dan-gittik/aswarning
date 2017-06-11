import setuptools


package = dict(
    name             = 'aswarning',
    version          = '0.1.0',
    author           = 'Dan Gittik',
    author_email     = 'dan.gittik@gmail.com',
    description      = 'A context manager that turns exceptions to warnings',
    license          = 'MIT',
    url              = 'https://github.com/dan-gittik/aswarning',
    packages         = setuptools.find_packages(),
    install_requires = [
    ],
    tests_require    = [
        'pytest',
    ],
)


if __name__ == '__main__':
	setuptools.setup(**package)
