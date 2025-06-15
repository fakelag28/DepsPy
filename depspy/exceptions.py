class DepsError(Exception):
    def __init__(self, error_code: str, error_message: str, error_id: str = None, status_code: int = None):
        self.error_code = error_code
        self.error_message = error_message
        self.error_id = error_id
        self.status_code = status_code
        super().__init__(f"{error_code}: {error_message}")

class UnauthorizedError(DepsError):
    def __init__(self, error_code: str = "UNAUTHORIZED", error_message: str = "Unauthorized", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 401)

class RateLimitError(DepsError):
    def __init__(self, error_code: str = "RATE_LIMIT_EXCEEDED", error_message: str = "Rate limit exceeded", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 429)

class PlayerNotFoundError(DepsError):
    def __init__(self, error_code: str = "PLAYER_NOT_FOUND", error_message: str = "Player not found", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 404)

class ServerNotFoundError(DepsError):
    def __init__(self, error_code: str = "SERVER_NOT_FOUND", error_message: str = "Server not found", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 404)

class InvalidRequestError(DepsError):
    def __init__(self, error_code: str = "INVALID_REQUEST", error_message: str = "Invalid request", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 400)

class APIError(DepsError):
    def __init__(self, error_code: str = "API_ERROR", error_message: str = "API error occurred", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 500)

class ConnectionError(DepsError):
    def __init__(self, error_code: str = "CONNECTION_ERROR", error_message: str = "Connection error occurred", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 0)

class TimeoutError(DepsError):
    def __init__(self, error_code: str = "TIMEOUT_ERROR", error_message: str = "Request timeout", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 408)

class ValidationError(DepsError):
    def __init__(self, error_code: str = "VALIDATION_ERROR", error_message: str = "Data validation error", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 422)

class MaintenanceError(DepsError):
    def __init__(self, error_code: str = "MAINTENANCE_ERROR", error_message: str = "API is under maintenance", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 503)

class InvalidAPIKeyError(UnauthorizedError):
    def __init__(self, error_code: str = "INVALID_API_KEY", error_message: str = "Invalid API key provided", error_id: str = None):
        super().__init__(error_code, error_message, error_id)

class ExpiredAPIKeyError(UnauthorizedError):
    def __init__(self, error_code: str = "EXPIRED_API_KEY", error_message: str = "API key has expired", error_id: str = None):
        super().__init__(error_code, error_message, error_id)

class InsufficientPermissionsError(UnauthorizedError):
    def __init__(self, error_code: str = "INSUFFICIENT_PERMISSIONS", error_message: str = "Insufficient permissions for this operation", error_id: str = None):
        super().__init__(error_code, error_message, error_id)

class InvalidServerIDError(InvalidRequestError):
    def __init__(self, error_code: str = "INVALID_SERVER_ID", error_message: str = "Invalid server ID provided", error_id: str = None):
        super().__init__(error_code, error_message, error_id)

class InvalidNicknameError(InvalidRequestError):
    def __init__(self, error_code: str = "INVALID_NICKNAME", error_message: str = "Invalid nickname provided", error_id: str = None):
        super().__init__(error_code, error_message, error_id)

class InvalidFractionIDError(InvalidRequestError):
    def __init__(self, error_code: str = "INVALID_FRACTION_ID", error_message: str = "Invalid fraction ID provided", error_id: str = None):
        super().__init__(error_code, error_message, error_id)

class CacheError(DepsError):
    def __init__(self, error_code: str = "CACHE_ERROR", error_message: str = "Cache error occurred", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 0)

class NetworkError(DepsError):
    def __init__(self, error_code: str = "NETWORK_ERROR", error_message: str = "Network error occurred", error_id: str = None):
        super().__init__(error_code, error_message, error_id, 0)

class ProxyError(NetworkError):
    def __init__(self, error_code: str = "PROXY_ERROR", error_message: str = "Proxy error occurred", error_id: str = None):
        super().__init__(error_code, error_message, error_id)

class SSLError(NetworkError):
    def __init__(self, error_code: str = "SSL_ERROR", error_message: str = "SSL error occurred", error_id: str = None):
        super().__init__(error_code, error_message, error_id)

class DNSResolutionError(NetworkError):
    def __init__(self, error_code: str = "DNS_RESOLUTION_ERROR", error_message: str = "DNS resolution error occurred", error_id: str = None):
        super().__init__(error_code, error_message, error_id) 