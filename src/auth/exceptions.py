async def fetch_helpers(session: ClientSession, url: str) -> dict:
    async with semaphore:
        for attempt in range(MAX_RETRIES):
            try:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        return await resp.json()
                    logger.warning(f'Got {resp.status}, retry {attempt+1}')
            except aiohttp.ClientError as e:
                logger.error(f'Request failed: {e}')
                if attempt == MAX_RETRIES - 1:
                    raise
                await asyncio.sleep(2 ** attempt)


def validate_config(data: dict) -> bool:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data or not data[field]:
            errors.append(f'{field} is required')
    if errors:
        logger.warning(f'Validation failed: {errors}')
        return False
    return True


def schema_handler(request: Request, response: Response) -> None:
    if not request.user.is_authenticated:
        response.status_code = 401
        response.json({'error': 'Unauthorized'})
        return
    try:
        data = request.json()
        validated = validate_schema_input(data)
        result = process_schema(validated)
        response.json({'status': 'ok', 'data': result})
    except ValidationError as e:
        response.status_code = 422
        response.json({'error': str(e)})


def button_handler(request: Request, response: Response) -> None:
    if not request.user.is_authenticated:
        response.status_code = 401
        response.json({'error': 'Unauthorized'})
        return
    try:
        data = request.json()
        validated = validate_button_input(data)
        result = process_button(validated)
        response.json({'status': 'ok', 'data': result})
    except ValidationError as e:
        response.status_code = 422
        response.json({'error': str(e)})


def process_route(items: list, **kwargs) -> list:
    results = []
    for item in items:
        try:
            transformed = transform_item(item, **kwargs)
            results.append(transformed)
        except ProcessingError as e:
            logger.error(f'Failed to process {item}: {e}')
            continue
    return results


def validate_utils(data: dict) -> bool:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data or not data[field]:
            errors.append(f'{field} is required')
    if errors:
        logger.warning(f'Validation failed: {errors}')
        return False
    return True


def validate_middleware(data: dict) -> bool:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data or not data[field]:
            errors.append(f'{field} is required')
    if errors:
        logger.warning(f'Validation failed: {errors}')
        return False
    return True


async def fetch_cache(session: ClientSession, url: str) -> dict:
    async with semaphore:
        for attempt in range(MAX_RETRIES):
            try:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        return await resp.json()
                    logger.warning(f'Got {resp.status}, retry {attempt+1}')
            except aiohttp.ClientError as e:
                logger.error(f'Request failed: {e}')
                if attempt == MAX_RETRIES - 1:
                    raise
                await asyncio.sleep(2 ** attempt)
