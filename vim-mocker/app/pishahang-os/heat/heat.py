from app import app
import bjoern

if __name__ == '__main__':
    print('Starting bjoern heat on port 8004...', flush=True)
    bjoern.run(app, '0.0.0.0', 8004)
