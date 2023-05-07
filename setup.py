from setuptools import setup, find_packages

setup(
    name='news_analyzer',
    version='1.0',
    author='Sunni Lin',
    email='sunni426@bu.edu',
    description='A news analyzer with authentication, uploader, feed ingester, and NLP modules',
    packages=find_packages(),
    install_requires=[
        'google-auth',
        'google-auth-oauthlib',
        'google-auth-httplib2',
        'feedparser',
        'nltk',
        'pandas',
        'numpy',
        'scikit-learn',
        'textblob'
    ],
    entry_points={
        'console_scripts': [
            'news_analyzer=news_analyzer.gui:main'
        ]
    }
)
