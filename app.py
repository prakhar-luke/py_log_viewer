from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Replace 'path/to/your/logfile.log' with the actual path to your log file
log_file_path = 'path/to/your/logfile.log'


def read_log_file():
    try:
        with open(log_file_path, 'r') as log_file:
            content = log_file.read()
        return content
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Log file not found")


@app.get("/", response_class=PlainTextResponse)
def read_log():
    return read_log_file()
