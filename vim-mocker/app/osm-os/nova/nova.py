from app import app
import bjoern

if __name__ == '__main__':
    print('Starting bjoern nova on port 8774...', flush=True)
    bjoern.run(app, '0.0.0.0', 9775)
