from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.models import User

app=create_app('production')
manager=Manager(app)
migrate = Migrate(app,db)
manager.add_command('server',Server)

manager.add_command('db',MigrateCommand)

# app.config['SECRET_KEY'] ='1234'
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://bashir:bashiir@localhost/pitch_perfect'

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
if __name__ == '__main__':
    manager.run()
