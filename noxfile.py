import nox
import tempfile

locations = 'src', 'tests', 'noxfile.py', 'docs/source/conf.py'
nox.options.sessions = 'tests', 'lint'



def install_with_constraints(session, *args, **kwargs):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            'poetry',
            'export',
            '--dev',
            '--format=requirements.txt',
            f'--output={requirements.name}',
            external=True
        )
        session.install(f'--constraint={requirements.name}', *args, **kwargs)
        # session.install is like `pip install`. So above uses version constraints using poetry



@nox.session(python=['3.8', '3.7'])
def tests(session):
    args = session.posargs or ['--cov']
    session.run('poetry', 'install','--no-dev', external=True)
    install_with_constraints(session, 'pytest', 'pytest-cov', 'coverage[toml]')
    session.run('pytest', *args)



@nox.session(python=['3.8', '3.7'])
def lint(session):
    args = session.posargs or locations
    install_with_constraints(session, 'pylint')

    # E0401 is import-error. -E is errors-only
    session.run('pylint', '-E', '--disable=E0401', 'src', *args)



@nox.session(python='3.8')
def docs(session):
    install_with_constraints(session, 'sphinx')
    session.run('sphinx-build', 'docs', 'docs/_build')



@nox.session(python='3.8')
def coverage(session):
    install_with_constraints(session, 'coverage[toml]', 'codecov')
    session.run('coverage', 'xml', '--fail-under=0')
    session.run('codecov', *session.posargs)