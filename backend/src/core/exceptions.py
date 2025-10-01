from fastapi import HTTPException, status


class BadRequestException(HTTPException):
    
    def __init__(self, detail):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail if detail else 'Bad request'
        )
        

class UnauthorizedException(HTTPException):
    
    def __init__(self, detail):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail if detail else 'Unauthorized'
        )
        

class ForbiddenException(HTTPException):
    
    def __init__(self, detail):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail if detail else 'Forbidden'
        )


class NotFoundException(HTTPException):
    
    def __init__(self, detail):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail if detail else 'Not found'
        )


class InternalServerErrorException(HTTPException):
    
    def __init__(self, detail):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail if detail else 'Internal server error'
        )
