from griptape.drivers import OpenAiAudioTranscriptionDriver

from .gtUIBaseDriver import gtUIBaseDriver

DEFAULT_API_KEY = "OPENAI_API_KEY"
DEFAULT_MODEL = "whisper-1"


class gtUIBaseAudioTranscriptionDriver(gtUIBaseDriver):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
            "optional": {},
        }

    RETURN_TYPES = ("DRIVER",)
    RETURN_NAMES = ("DRIVER",)

    FUNCTION = "create"

    CATEGORY = "Griptape/Drivers/Audio Transcription"

    def create(
        self,
    ):
        api_key = self.getenv(DEFAULT_API_KEY)
        params = {}

        if api_key:
            params["api_key"] = api_key
        params["model"] = DEFAULT_MODEL
        driver = OpenAiAudioTranscriptionDriver(**params)
        return (driver,)
