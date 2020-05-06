from app import app
import bjoern

if __name__ == '__main__':
    print('Starting bjoern glance on port 10243...', flush=True)
    bjoern.run(app, '0.0.0.0', 10243)
