from __future__ import annotations

from apollo.models.adapters.local_echo_adapter import LocalEchoAdapter
from apollo.models.adapters.ollama_adapter import OllamaAdapter
from apollo.models.adapters.koboldcpp_adapter import KoboldCppAdapter
from apollo.models.adapters.openai_compatible_adapter import OpenAICompatibleAdapter
from apollo.models.adapters.text_generation_webui_adapter import TextGenerationWebUIAdapter
from apollo.models.model_registry import ModelProfile, ModelRegistry


class ModelRouter:
    def __init__(self, settings):
        self.settings = settings
        self.registry = ModelRegistry(settings.model_sources_path)

    def select_model(self, task_analysis):
        key = task_analysis.required_model
        fallback_model_name = {
            "coding": self.settings.coding_model,
            "reasoning": self.settings.reasoning_model,
            "writing": self.settings.writing_model,
            "default": self.settings.default_model,
        }.get(key, self.settings.default_model)
        profile = self.registry.find_for_role(
            role=key,
            provider=self.settings.model_provider,
            model_id=self.settings.model_id or fallback_model_name,
        )
        if not profile:
            profile = ModelProfile(
                id=f"{self.settings.model_provider}:{fallback_model_name}",
                provider=self.settings.model_provider,
                model=fallback_model_name,
                role=key,
            )
        return self._adapter_for_profile(profile)

    def _adapter_for_profile(self, profile: ModelProfile):
        provider = profile.provider
        model_name = profile.model
        base_url = profile.base_url

        if self.settings.use_ollama or provider == "ollama":
            return OllamaAdapter(model_name=model_name, host=self.settings.ollama_host)
        if provider == "lmstudio":
            return OpenAICompatibleAdapter(model_name=model_name, base_url=base_url or self.settings.lmstudio_base_url, provider="lmstudio")
        if provider == "vllm":
            return OpenAICompatibleAdapter(model_name=model_name, base_url=base_url or self.settings.vllm_base_url, provider="vllm")
        if provider == "localai":
            return OpenAICompatibleAdapter(model_name=model_name, base_url=base_url or self.settings.localai_base_url, provider="localai")
        if provider == "openai_compatible":
            return OpenAICompatibleAdapter(
                model_name=model_name,
                base_url=base_url or self.settings.openai_compatible_base_url,
                api_key=self.settings.openai_compatible_api_key,
                provider="openai_compatible",
            )
        if provider == "textgen-webui":
            return TextGenerationWebUIAdapter(model_name=model_name, base_url=base_url or self.settings.textgen_base_url)
        if provider == "koboldcpp":
            return KoboldCppAdapter(model_name=model_name, base_url=base_url or self.settings.koboldcpp_base_url)
        return LocalEchoAdapter(model_id=f"{provider or 'local'}:placeholder:{model_name}")
