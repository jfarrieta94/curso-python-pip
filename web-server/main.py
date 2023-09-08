import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4]

@app.get('/contact', response_class = HTMLResponse)
def get_list():
    return """
    <h1>Larlitos, si lees esto, eres gay</h1>
    <p>Larloncio es raroncio</p>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()