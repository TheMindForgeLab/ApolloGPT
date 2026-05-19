from __future__ import annotations

from apollo.models.adapters.local_echo_adapter import LocalEchoAdapter
from apollo.models.adapters.ollama_adapter import OllamaAdapter
from apollo.models.adapters.koboldcpp_adapter import KoboldCppAdapter
from apollo.models.adapters.openai_compatible_adapter import OpenAICompatibleAdapter
from apollo.models.adapters.text_generation_webui_adapter import TextGenerationWebUIAdapter


class ModelRouter:
    def __init__(self, settings):
        self.settings = settings

    def select_model(self, task_analysis):
        key = task_analysis.required_model
        model_name = {
            "coding": self.settings.coding_model,
            "reasoning": self.settings.reasoning_model,
            "writing": self.settings.writing_model,
            "default": self.settings.default_model,
        }.get(key, self.settings.default_model)

        if self.settings.use_ollama or self.settings.model_provider == "ollama":
            return OllamaAdapter(model_name=model_name, host=self.settings.ollama_host)
        if self.settings.model_provider == "lmstudio":
            return OpenAICompatibleAdapter(model_name=model_name, base_url=self.settings.lmstudio_base_url, provider="lmstudio")
        if self.settings.model_provider == "vllm":
            return OpenAICompatibleAdapter(model_name=model_name, base_url=self.settings.vllm_base_url, provider="vllm")
        if self.settings.model_provider == "localai":
            return OpenAICompatibleAdapter(model_name=model_name, base_url=self.settings.localai_base_url, provider="localai")
        if self.settings.model_provider == "openai_compatible":
            return OpenAICompatibleAdapter(
                model_name=model_name,
                base_url=self.settings.localai_base_url,
                api_key=self.settings.openai_compatible_api_key,
                provider="openai_compatible",
            )
        if self.settings.model_provider == "textgen-webui":
            return TextGenerationWebUIAdapter(model_name=model_name, base_url=self.settings.textgen_base_url)
        if self.settings.model_provider == "koboldcpp":
            return KoboldCppAdapter(model_name=model_name, base_url=self.settings.koboldcpp_base_url)
        return LocalEchoAdapter(model_id=f"local:placeholder:{model_name}")
