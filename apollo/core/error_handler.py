class ApolloError(Exception):
    pass


class ErrorHandler:
    def handle(self, exc: Exception) -> dict:
        return {"error": exc.__class__.__name__, "message": str(exc)}

