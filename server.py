from app import app;
import os;
if __name__ == '__main__':
    app.run(host="localhost", port=os.getenv('PORT') if os.getenv('PORT') else 5000, debug=True)