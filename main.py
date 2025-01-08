import uuid
import time
import traceback
import logger
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

# Custom imports
from routers import admin_router

# Create FastAPI app
app = FastAPI(
    title='Fast API template',
    description="Boilerplate code for fast API",
    version='1.0.0'
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def measure_request(request: Request, call_next):
    """ Measure request time and memory """
    with logger.contextualize(request_id=uuid.uuid4()):
        # Start time and request path
        start_time = time.perf_counter()
        path, method = request.url.path, request.method
        logger.info(f'Process Started for {method} {path}')

        # Suppress all errors as we do not want scheduler to retry failed process
        try:
            response = await call_next(request)
        except:
            traceback.print_exc()
            response = PlainTextResponse('Failed')

        logger.info((f'Process Ended for {method} {path} | Time taken (sec): '
                     f'{round(time.perf_counter() - start_time, 2)} | {get_memory_usage()}'))

        return response


@app.get('/')
def home():
    """ Application Home """
    logger.debug('Home Get Method called...')
    return 'Success'


# Add routers
app.include_router(admin_router.router, prefix='/admin', tags=['dv360'])
# app.include_router(cm360.router, prefix='/cm360', tags=['cm360'])

