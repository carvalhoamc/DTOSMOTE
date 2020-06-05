from distutils.core import setup

setup(
		name='dtosmote',
		packages=['dtosmote'],
		version='1.0.3',
		license='MIT',
		description='Delaunay Thetraedral Oversampling - DTOSMOTE',
		long_description= 'Oversampling creates synthetic or duplicate minority class sam- ples to match the same number of'
		            ' samples from the majority class. As a result, the training data set becomes balanced before the'
		            ' training phase. DTO-SMOTE constructs a mesh of simplices for creating synthetic examples.',
		author='Alexandre Miguel de Carvalho & Ronaldo Cristiano Prati',
		author_email='carvalho.alexandre@ufabc.edu.br',
		url='https://github.com/carvalhoamc/DTOSMOTE',
		download_url='https://github.com/carvalhoamc/DTOSMOTE/archive/v1.0.3.tar.gz',
		keywords=['oversampling', 'smote', 'geosmote', 'dto', 'dtosmote'],
		install_requires=[
			'scikit-learn',
			'imbalanced-learn',
			'scipy',
			'numpy',
			'pandas'
		],
		classifiers=[  # Optional
			# How mature is this project? Common values are
			#   3 - Alpha
			#   4 - Beta
			#   5 - Production/Stable
			'Development Status :: 5 - Production/Stable',
			
			# Indicate who your project is intended for
			'Intended Audience :: Developers',
			'Topic :: Software Development :: Build Tools',
			
			# Pick your license as you wish
			'License :: OSI Approved :: MIT License',
			
			# Specify the Python versions you support here. In particular, ensure
			# that you indicate whether you support Python 2, Python 3 or both.
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.4',
			'Programming Language :: Python :: 3.5',
			'Programming Language :: Python :: 3.6',
		],
)
