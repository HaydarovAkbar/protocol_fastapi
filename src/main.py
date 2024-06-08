from fastapi import FastAPI
# from routers.api import router # add this later
from utils.__init_db import create_tables


app = FastAPI(
    debug=True,
    title="Tutorial",
)


@app.on_event("startup")
def on_startup() -> None:
    """
    Initializes the database tables when the application starts up.
    """
    create_tables()


# app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)