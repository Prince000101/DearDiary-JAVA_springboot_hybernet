def validate_serializer(data: dict) -> bool:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data or not data[field]:
            errors.append(f'{field} is required')
    if errors:
        logger.warning(f'Validation failed: {errors}')
        return False
    return True


def validate_logger(data: dict) -> bool:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data or not data[field]:
            errors.append(f'{field} is required')
    if errors:
        logger.warning(f'Validation failed: {errors}')
        return False
    return True


def query_handler(request: Request, response: Response) -> None:
    if not request.user.is_authenticated:
        response.status_code = 401
        response.json({'error': 'Unauthorized'})
        return
    try:
        data = request.json()
        validated = validate_query_input(data)
        result = process_query(validated)
        response.json({'status': 'ok', 'data': result})
    except ValidationError as e:
        response.status_code = 422
        response.json({'error': str(e)})
