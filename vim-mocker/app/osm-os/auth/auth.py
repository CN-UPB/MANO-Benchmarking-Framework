from app import app
import bjoern

if __name__ == '__main__':
    print('Starting bjoern auth on port 5000...', flush=True)
    bjoern.run(app, '0.0.0.0', 6001)
