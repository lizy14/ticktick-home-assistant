"""Config flow for TickTick Integration."""

import logging

import voluptuous as vol
from homeassistant.config_entries import ConfigEntry, OptionsFlow
from homeassistant.core import callback
from homeassistant.helpers import config_entry_oauth2_flow

from .const import CONF_API_ENDPOINT, DEFAULT_API_ENDPOINT, DOMAIN


def _validate_api_endpoint(value: str) -> str:
    """Validate that an API endpoint uses HTTPS."""
    if not value.startswith("https://"):
        raise vol.Invalid(
            "API endpoint must use HTTPS protocol (e.g., https://api.example.com)"
        )
    return value


API_ENDPOINT_SCHEMA = vol.All(vol.Url(), _validate_api_endpoint)


class OAuth2FlowHandler(
    config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN
):
    """Config flow to handle TickTick Integration OAuth2 authentication."""

    DOMAIN = DOMAIN

    def __init__(self) -> None:
        """Initialize the config flow."""
        super().__init__()
        self._api_endpoint = DEFAULT_API_ENDPOINT

    async def async_step_user(self, user_input=None):
        """Configure the API endpoint before authentication."""
        if user_input is not None:
            self._api_endpoint = user_input[CONF_API_ENDPOINT]
            return await self.async_step_pick_implementation()

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_API_ENDPOINT, default=DEFAULT_API_ENDPOINT
                    ): API_ENDPOINT_SCHEMA,
                }
            ),
        )

    async def async_oauth_create_entry(self, data):
        """Create an entry with the selected API endpoint."""
        return self.async_create_entry(
            title=self.flow_impl.name,
            data=data,
            options={CONF_API_ENDPOINT: self._api_endpoint},
        )

    @property
    def logger(self) -> logging.Logger:
        """Return logger."""
        return logging.getLogger(__name__)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow:
        """Return the options flow."""
        return OptionsFlowHandler(config_entry)


class OptionsFlowHandler(OptionsFlow):
    """Handle TickTick options."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        """Initialize the options flow."""
        self._config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the TickTick options."""
        if user_input is not None:
            return self.async_create_entry(data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_API_ENDPOINT,
                        default=self._config_entry.options.get(
                            CONF_API_ENDPOINT, DEFAULT_API_ENDPOINT
                        ),
                    ): API_ENDPOINT_SCHEMA,
                }
            ),
        )
