try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='readlater',
    version='0.1',
    description='ReadLater with relevance',
    author='Shivanand Velmurugan',
    author_email='me@shiv.me',
    url='http://rl.shiv.me/',
    install_requires=[
        "Pylons>=0.9.7",
        "SQLAlchemy>=0.5",
		"docutils==0.4",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'readlater': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'readlater': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = readlater.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
